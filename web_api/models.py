from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


class banner(models.Model):
    banner_1 = models.ImageField(
        upload_to='images/%Y/%m/%d', null=True, blank=True)
    banner_2 = models.ImageField(
        upload_to='images/%Y/%m/%d', null=True, blank=True)
    banner_3 = models.ImageField(
        upload_to='images/%Y/%m/%d', null=True, blank=True)
    banner_4 = models.ImageField(
        upload_to='images/%Y/%m/%d', null=True, blank=True)


class menu(models.Model):
    """ Home landing page apis """
    Home = models.CharField(max_length=255)
    Aboutus = models.CharField(max_length=255)
    OurServices = models.CharField(max_length=255)
    FAQ = models.CharField(max_length=255)
    Blog = models.CharField(max_length=255)
    ContactUs = models.CharField(max_length=255)
    Login = models.CharField(max_length=255)
    Register = models.CharField(max_length=255)


class home_body(models.Model):
    """ Home landing page apis """
    WhatisThinkAhoy_title = models.CharField(max_length=255)
    WhatisThinkAhoy_desc = models.CharField(max_length=550)
    big_img = models.ImageField(
        upload_to='images/%Y/%m/%d', null=True, blank=True)
    TheThinkAhoyMission_title = models.CharField(max_length=255)
    TheThinkAhoyMission_desc_1 = models.CharField(max_length=550)
    TheThinkAhoyMission_desc_2 = models.CharField(max_length=550)
    JoinhandsinThinkAhoymission_title = models.CharField(max_length=250)
    JoinhandsinThinkAhoymission_number = models.CharField(max_length=250)
    JoinhandsinThinkAhoymission_dec = models.CharField(max_length=250)


class footer(models.Model):
    """ Home landing page apis """
    UsefulLink_title = models.CharField(max_length=255)
    Home = models.CharField(max_length=255)
    Aboutus = models.CharField(max_length=255)
    OurServices = models.CharField(max_length=255)
    FAQ = models.CharField(max_length=255)
    Blog = models.CharField(max_length=255)
    ContactUs = models.CharField(max_length=255)
    NeedHelp_title = models.CharField(max_length=255)
    privacypolicy = models.CharField(max_length=255)
    termsconditions = models.CharField(max_length=255)


class homeapi(models.Model):
    """ Home landing page apis """
    menudata = models.OneToOneField(menu, on_delete=models.CASCADE)
    banner = models.OneToOneField(banner, on_delete=models.CASCADE)
    home_content = models.OneToOneField(home_body, on_delete=models.CASCADE)
    footer_menu = models.OneToOneField(footer, on_delete=models.CASCADE)
