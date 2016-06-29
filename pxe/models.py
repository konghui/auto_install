#coding=utf-8
from django.db import models
import django.utils.timezone

# Create your models here.
raid_chose = ((False,'不可安装'),(True,'可安装'))
ETH = (('eth0','eth0'),('eth1','eth1'))
raid_level = ((1,'raid1'),(0,'raid0'),(5,'raid5'))
ks_choices = (('conf','测试ks勿安装'),('webserver','webserver'))
stripe_choices = ((1024,'1M'),(512,'512K'),(128,'128K'),(64,'64K'))
netmask=(("255.255.0.0","255.255.0.0"),("255.255.255.0","255.255.255.0"),('255.255.255.128','255.255.255.128'),('255.255.255.192','255.255.255.192'),('255.255.255.224','255.255.255.224'),('255.255.255.240','255.255.255.240'))
class disk_sotl(models.Model):
    sotl = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    host_id = models.IntegerField()
    
class install(models.Model):
    inc = models.CharField(max_length=30)
    ilo_ip = models.GenericIPAddressField(null=True,blank=True)
    ilo_netmask = models.GenericIPAddressField(null=True,blank=True)
    ilo_gw = models.GenericIPAddressField(null=True,blank=True)
    ipaddr = models.GenericIPAddressField()
    sn = models.CharField(max_length=100,unique=True)
    status = models.BooleanField(default=True,choices=raid_chose)
    day = models.DateField(default=django.utils.timezone.now)
    cpu = models.CharField(max_length=100,)
    mem = models.CharField(max_length=20,)
    sotl = models.CharField(max_length=5)
    ksdev = models.CharField(max_length=10)
    def __unicode__(self):
        return "%s " % self.ipaddr
class online(models.Model):
    level = models.IntegerField(choices=raid_level,blank=False,default=1)
    ip = models.GenericIPAddressField()
    service_ip = models.GenericIPAddressField(null=True,blank=True)
    service_netmask = models.CharField(max_length=30,choices=netmask,default="255.255.255.0",blank=False)
    service_gw = models.GenericIPAddressField(null=True,blank=True)
    ilo_ip = models.GenericIPAddressField(null=True,blank=True)
    ilo_netmask = models.CharField(max_length=30,choices=netmask,default="255.255.0.0",blank=False,null=True)
    ilo_gw = models.GenericIPAddressField(null=True,blank=True)    
    status = models.BooleanField(default=False)
    inc = models.CharField(max_length=30)
    sn = models.CharField(max_length=100,unique=True)
    sotl_total = models.IntegerField()
    stripe = models.IntegerField(default='1024',blank=False,choices=stripe_choices)
    raid_zh = models.CharField(max_length=200,)
    kickstart = models.CharField(max_length=30,blank=False,default='webserver',choices=ks_choices)
    finish_status = models.BooleanField(default=False)
    jindu = models.IntegerField(default=0)
    eth = models.CharField(max_length=10,choices=ETH,default='eth0',blank=False)
    ssh_status = models.BooleanField(default=False)
    ksdev = models.CharField(max_length=10)
    def __unicode__(self):
        return "%s" % self.ip
    
class ilo_table(models.Model):
    maunfacturer = models.CharField(max_length=100,)
    lan_num = models.IntegerField()
    def __unicode__(self):
        return "%s" % self.maunfacturer
