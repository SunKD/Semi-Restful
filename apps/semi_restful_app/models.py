# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        print postData
        if postData['first_name'] == "":
            errors["first_name"]= "Name should be more than 1 characters"
        if postData['last_name'] == "":
            errors["last_name"]= "Name should be more than 1 characters"
        if postData['email'] == "":
            errors["email"] = "Email should be more than 5characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email Should contain one upper letter, one lowerletter and number "
        return errors
        
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{}, {}, {}'.format(self.first_name, self.last_name, self.email)
    objects = UserManager()