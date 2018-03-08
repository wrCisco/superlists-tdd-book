#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

from django.contrib import auth
from django.db import models

# Create your models here.


auth.signals.user_logged_in.disconnect(auth.models.update_last_login)


class User(models.Model):
    email = models.EmailField(primary_key=True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    uid = models.CharField(max_length=40, default=uuid.uuid4)
    email = models.EmailField()

