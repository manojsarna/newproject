# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
 
from app.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django import template
from django.contrib import messages
import datetime


@login_required(login_url="/login/")
def index(request):
    print(request.user)
    now = datetime.datetime.now()
    c_yr = int(now.strftime('%Y'))
    c_yr_1= int(now.strftime('%Y'))+1
    print(c_yr)
    print(c_yr_1)
    c_yr_10 = int(c_yr) - 10
    lityear = list(range(c_yr_10, c_yr_1))
     
    city=list(demo_data.objects.filter(user=request.user).values('city','year').order_by('-id'))

    if len(city)>0:
        city_pass = city[0]['city']
        year_pass=city[0]['year']
    else:
        city_pass_str = list(UserWithcity.objects.filter(user_id=request.user).values())  
        city_pass =city_pass_str[0]['city_name']
        year_pass = c_yr


    obj=demo_data.objects.filter(city=city_pass,year=year_pass).first()

    usercity=list(UserWithcity.objects.filter(user_id=request.user).values())

    # j=list(demo_data.objects.filter(city='Delhi',year=2021).values())
    print(city_pass,year_pass,)
    
    print(obj)
    print(usercity)

    request.session['city'] = city_pass
    request.session['year'] = year_pass
     
    
    context = {
        'obj':obj,
        'ucity':usercity,
        'city':city_pass,
        'year': lityear[::-1],
        'syear': year_pass,
    }


    context['segment'] = 'index'
   
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        


    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


 

  
 

    
 
@login_required(login_url="/auth_user/")

def getAuthUser(request):
    
    obj=AuthUser.objects.all()
    context = {
        'obj':obj
    }
    
    html_template = loader.get_template( 'authuserlist.html')    
    return HttpResponse(html_template.render(context, request))



@login_required(login_url="/maindashboard/")
def maindashboard(request):    

    obj=AuthUser.objects.all()  

    context = {
        # 'obj':obj
    }

    if request.method=="POST":
        year=request.POST.get('year')
        city=request.POST.get('city')
        flag=request.POST.get('total')        
        demo_1=request.POST.get('demo_1')
        demo_2=request.POST.get('demo_2')
        demo_3=request.POST.get('demo_3')
        demo_4=request.POST.get('demo_4')
        demo_5=request.POST.get('demo_5')
        demo_6=request.POST.get('demo_6')
        demo_7=request.POST.get('demo_7')
        demo_8=request.POST.get('demo_8')
        demo_9=request.POST.get('demo_9')
        demo_10=request.POST.get('demo_10')
        demo_11=request.POST.get('demo_11')
        demo_12=request.POST.get('demo_12')
        demo_13=request.POST.get('demo_13')
        demo_14=request.POST.get('demo_14')
        demo_15=request.POST.get('demo_15')
        demo_16=request.POST.get('demo_16')
        demo_17=request.POST.get('demo_17')
        demo_18=request.POST.get('demo_18')
        demo_19=request.POST.get('demo_19')
        demo_20=request.POST.get('demo_20')
        user=request.user
        # try:
        print('flag',flag)
        print('city',city)
        print('year',year)
        if flag=='0':
            ob=demo_data(year=year,city=city,demo_1=demo_1,demo_2=demo_2,demo_3=demo_3,demo_4=demo_4,demo_5=demo_5,demo_6=demo_6,demo_7=demo_7,
            demo_8=demo_8,demo_9=demo_9,demo_10=demo_10,demo_11=demo_11,demo_12=demo_12,demo_13=demo_13,demo_14=demo_14,demo_15=demo_15,demo_16=demo_16,demo_17=demo_17,demo_18=demo_18,demo_19=demo_19,demo_20=demo_20,user=user)
            ob.save()
            messages.success(request, 'Successfully Done!')
        else: 
            demo_data.objects.filter(year=year,city=city,user=user).update(demo_1=demo_1,demo_2=demo_2,demo_3=demo_3,demo_4=demo_4,demo_5=demo_5,demo_6=demo_6,demo_7=demo_7,
            demo_8=demo_8,demo_9=demo_9,demo_10=demo_10,demo_11=demo_11,demo_12=demo_12,demo_13=demo_13,demo_14=demo_14,demo_15=demo_15,demo_16=demo_16,demo_17=demo_17,demo_18=demo_18,demo_19=demo_19,demo_20=demo_20)
             
        # except:
        #     html_template = loader.get_template( 'index.html' )
        #     return HttpResponse(html_template.render(context, request))

    
    
    html_template = loader.get_template( 'maindashboard.html')    
    return HttpResponse(html_template.render(context, request))


def getdemoInfo(request):
    if request.method == "GET" and request.is_ajax():
        city=request.GET.get('city')
        year=request.GET.get('year')        
        obj=list(demo_data.objects.filter(city=city,year=year).values())
        print(obj)
        context = {
            'obj':obj
        }

        return JsonResponse(context, status=200)
    return JsonResponse({"success":False}, status=400)


  
@login_required(login_url="/login/")
def module1_form(request):   
     
    dat=[]    
    year= request.session['year']
    city= request.session['city']    
    # city='Bhopal'             
    ob= DataPoint_Indicator.objects.filter(city=city,year=year,user=request.user).values()
    obj1=Modules_indicator.objects.filter(m_code='UPS').values().order_by('id')

    if ob:
        flag=1
        for o in range(len(obj1)):   
            obj2=list(DataPoint_Indicator.objects.filter(m_code='UPS',indicator=obj1[o]['number'],user=request.user).values())         
            # print(obj2)      
            dat.append({"m_code":'UPS','category':obj1[o]['category'],'typeofindicator':obj1[o]['type_of_indicator'],'no':obj1[o]['number'],'indicator':obj1[o]['indicator'],'datapoint':obj2})
        
    else:   
        flag=0
        for o in range(len(obj1)):  
            print(obj1[o]['category'],obj1[o]['type_of_indicator'])
            obj2=list(Point_Indicator.objects.filter(m_code='UPS',indicator=obj1[o]['number']).values())
            dat.append({"m_code":'UPS','category':obj1[o]['category'],'typeofindicator':obj1[o]['type_of_indicator'],'no':obj1[o]['number'],'indicator':obj1[o]['indicator'],'datapoint':obj2})
        
    # print(dat)
    print('flag',flag)
    context = {'data':dat,'flag':flag}
    
    # print('len(dat)',len(dat))

    if request.method=="POST":  
        user=request.user
        for i in dat:             
            # m_code=dat[i]['m_code']
            m_code='UPS'
            s_ind=i['no']
            datapoint=i['datapoint'] 
            # print(datapoint)  
            # print('adasa')  
            for k in datapoint:                
                p_id=k['p_id']
                input_type=k['input_type']
                p='p_'+str(k['indicator'])+ str(k['p_id'])
                r='r_'+str(k['indicator'])+ str(k['p_id'])
                f='f_'+str(k['indicator'])+ str(k['p_id'])
                p_desc=k['point_desc']
                                 
                pvalue=request.POST.get(p)
                remark=request.POST.get(r)
                file=request.POST.get(f)
                if file==None:
                    # print('kkms')
                    file=request.FILES[f] 
                # print('filemanagement',file)
                # if file==None:
                #     file=''
                if flag==0:

                    data= DataPoint_Indicator(p_id=p_id,m_code=m_code,indicator=s_ind,
                        point_desc=p_desc,point_value=pvalue,point_remark=remark,point_attach=file,input_type=input_type,
                            city=city,year=year, user=request.user)
                    data.save()

                    messages.success(request, 'Successfully Created!')

                else:

                    DataPoint_Indicator.objects.filter(p_id=p_id,m_code=m_code,city=city,year=year).update(indicator=s_ind,
                        point_desc=p_desc,point_value=pvalue,point_remark=remark,point_attach=file,user=request.user)

        
        return redirect('module1_form')

    # context['segment'] = 'module1/'  

    html_template = loader.get_template( 'module1/entry-form.html')
    
    return HttpResponse(html_template.render(context, request))
