# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import AutoField
 

 
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)    
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'auth_user'



class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

 
 
 


class Modules(models.Model) :    
    m_code=models.TextField(primary_key=True,max_length=10,blank=True)
    m_desc=models.TextField(max_length=150,blank=True,null=True)    
    s_no=models.IntegerField(blank=True,null=True)     
    class Meta:       
        db_table = 'modules_mst'

class Modules_indicator(models.Model) :
    m_code=models.ForeignKey(Modules,db_column='m_code',on_delete=models.CASCADE, null=True)
    number=models.FloatField(blank=True,null=True)     
    sub_theme=models.TextField(max_length=150,blank=True,null=True)
    indicator=models.TextField(max_length=150,blank=True,null=True)
    formula=models.TextField(max_length=150,blank=True,null=True)
    unit=models.TextField(max_length=150,blank=True,null=True)
    benchmark=models.TextField(max_length=150,blank=True,null=True)
    source_of_benchmark=models.TextField(max_length=150,blank=True,null=True)
    category=models.TextField(max_length=150,blank=True,null=True)
    type_of_indicator=models.TextField(max_length=150,blank=True,null=True)
    
    class Meta:       
        db_table = 'modules_indicator_mst'


        
class Point_Indicator(models.Model) :
    p_id=models.AutoField(primary_key=True)  
    m_code=models.ForeignKey(Modules,db_column='m_code',on_delete=models.CASCADE, null=True)   
    indicator=models.TextField(max_length=150,blank=True,null=True)
    point_desc=models.TextField(max_length=150,blank=True,null=True)   
    input_type=models.TextField(max_length=150,blank=True,null=True) 

    class Meta:       
        db_table = 'point_indicator_mst'


class DataPoint_Indicator(models.Model) :
    s_id=models.AutoField(primary_key=True)  
    p_id=models.TextField(max_length=5,blank=True,null=True) 
    # m_code=models.ForeignKey(Modules,db_column='m_code',on_delete=models.CASCADE, null=True)   
    m_code=models.TextField(max_length=150,blank=True,null=True)
    indicator=models.TextField(max_length=150,blank=True,null=True)
    point_desc=models.TextField(max_length=150,blank=True,null=True)  
    point_value=models.TextField(max_length=150,blank=True,null=True) 
    point_remark=models.TextField(max_length=150,blank=True,null=True)  
    point_attach=models.FileField(upload_to='module1',blank=True,null=True)
    input_type=models.TextField(max_length=150,blank=True,null=True) 
    city=models.TextField(max_length=50,blank=True,null=True) 
    year=models.TextField(max_length=4,blank=True,null=True) 
    user=models.TextField(max_length=150,blank=True,null=True)
    last_modified=models.DateTimeField(auto_now=True,blank=True) 
    
    class Meta:       
        db_table = 'datapoint_indicator_mst'
        unique_together = (('p_id', 'city','year','m_code'),)



class demo_data(models.Model) :
    year=models.IntegerField(blank=True,null=True)
    city=models.TextField(max_length=100,blank=True,null=True)
    demo_1=models.TextField(max_length=150,blank=True,null=True)
    demo_2=models.TextField(max_length=150,blank=True,null=True)
    demo_3=models.TextField(max_length=150,blank=True,null=True)
    demo_4=models.TextField(max_length=150,blank=True,null=True)
    demo_5=models.TextField(max_length=150,blank=True,null=True)
    demo_6=models.TextField(max_length=150,blank=True,null=True)
    demo_7=models.TextField(max_length=150,blank=True,null=True)
    demo_8=models.TextField(max_length=150,blank=True,null=True)
    demo_9=models.TextField(max_length=150,blank=True,null=True)
    demo_10=models.TextField(max_length=150,blank=True,null=True)
    demo_11=models.TextField(max_length=150,blank=True,null=True)
    demo_12=models.TextField(max_length=150,blank=True,null=True)
    demo_13=models.TextField(max_length=150,blank=True,null=True)
    demo_14=models.TextField(max_length=150,blank=True,null=True)
    demo_15=models.TextField(max_length=150,blank=True,null=True)
    demo_16=models.TextField(max_length=150,blank=True,null=True)
    demo_17=models.TextField(max_length=150,blank=True,null=True)
    demo_18=models.TextField(max_length=150,blank=True,null=True)
    demo_19=models.TextField(max_length=150,blank=True,null=True)
    demo_20=models.TextField(max_length=150,blank=True,null=True)
    user=models.TextField(max_length=150,blank=True,null=True)
    last_modified=models.DateTimeField(auto_now=True,blank=True)    
    class Meta:       
        db_table = 'demo_data'
        unique_together = (('year','city'),)



class City_mst(models.Model):    
    city_code=models.TextField(primary_key=True,max_length=10,blank=True)
    city_name=models.TextField(max_length=150,blank=True,null=True)  
    class Meta:       
        db_table = 'city_mst'

        
class UserWithcity(models.Model):
    s_no =models.AutoField(primary_key=True)
    user_id=models.TextField(max_length=10,blank=True)
    city_name=models.TextField(max_length=150,blank=True,null=True)  
    class Meta:       
        db_table = 'userwithcity'
        unique_together = (('user_id','city_name'),)