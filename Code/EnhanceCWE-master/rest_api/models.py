# @OPENSOURCE_HEADER_START@
# MORE Tool 
# Copyright 2016 Carnegie Mellon University.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED "AS IS," WITH NO WARRANTIES WHATSOEVER.
# CARNEGIE MELLON UNIVERSITY EXPRESSLY DISCLAIMS TO THE FULLEST EXTENT
# PERMITTEDBY LAW ALL EXPRESS, IMPLIED, AND STATUTORY WARRANTIES,
# INCLUDING, WITHOUT LIMITATION, THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT OF PROPRIETARY
# RIGHTS.
#
# Released under a modified BSD license, please see license.txt for full
# terms. DM-0003473
# @OPENSOURCE_HEADER_END@
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from register_approval.signals import register_approved, register_rejected
from django.db import models
from django.core.validators import URLValidator
from solo.models import SingletonModel
from django.contrib import admin
from base.models import BaseModel


@receiver(register_approved)
def create_auth_token(sender, instance, **kwargs):
    """
    Create the token once the user is approved.
    """
    if getattr(instance, 'requested_role', None) == 'client':
        Token.objects.create(user=instance.user)


@receiver(register_rejected)
def delete_auth_token(sender, instance, **kwargs):
    """
    delete the token once the user is rejected.
    """
    Token.objects.filter(user=instance.user).delete()


class RESTConfiguration(BaseModel):
    name = models.CharField(max_length=32)
    url = models.CharField(validators=[URLValidator()], max_length=255)
    token = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "REST Configuration"
