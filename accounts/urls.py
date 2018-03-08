#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import send_login_email, login

urlpatterns = [
    url(r'^send_login_email$', send_login_email, name='send_login_email'),
    url(r'^login$', login, name='login'),
]

