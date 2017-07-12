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
from django.shortcuts import render
from mailer.util import send_email
from django.conf import settings
from django.contrib.auth.models import User
from django.template import Context
from django.http import Http404, JsonResponse

# Home screen
def index(request):
    return render(request, 'frontpage/index.html')

def process_contact_us(request):
    if request.method == 'POST':

        subject = request.POST['subject']
        content = request.POST['content']

        if not subject:
            raise Http404("Subject cannot be empty!\n")

        if not request.POST['user_name']:
            sender_name = "anonymous"
        else:
            sender_name = request.POST['user_name']

        message = "sender's name: "+request.POST['user_name']+"\n"

        if request.POST['user_email']:
            message += "sender's email: "+request.POST['user_email']+"\n"

        message += "subject: "+subject+"\n"
        message += "content: "+content+"\n"

        superuser = User.objects.get(is_superuser = True)
        
        send_email(subject=subject, users = [superuser], message=message,
            context=Context({'username': superuser.username, 'body': message}))

        return JsonResponse({'succ':True})
    else:
        raise Http404("Service not Available\n")