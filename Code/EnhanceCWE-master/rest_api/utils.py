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
import requests
from requests.exceptions import ConnectionError
from .models import *
import json


class rest_api:

    @staticmethod
    def get_url(name):
        '''
        Returns the URL of REST API server
        :return: A string containing the URL
        '''
        if RESTConfiguration.objects.all().filter(name = name):
            config = RESTConfiguration.objects.all().filter(name = name)[0]
            return config.url
        else:
            return None

    @staticmethod
    def get_header(name):
        '''
        Creates a dictionary of the things to be passed in the REST requests header
        :return: A dictionary containing the API key
        '''
        if RESTConfiguration.objects.all().filter(name = name):
            config = RESTConfiguration.objects.all().filter(name = name)[0]
            return {'Authorization': 'Token %s' % config.token}
        else:
            return {}

    @staticmethod
    def process_response(response):
        '''
        This method process the response for errors or success
        :param response: Response object that's been returned from the server
        :return: A dictionary containing the following three key-values:
         success: A boolean value representing whether request to the server was successful or not
         msg: A string containing a descriptive message about what happened with the request
         obj: Any additional object (generally the JSON object) if some data is to be returned to the caller.
        '''
        success = False
        msg = None
        obj = None
        if response.status_code == requests.codes.unauthorized:
            # Authentication Failure
            msg = 'Authentication Failure. All requests must be authenticated with a valid API Key. ' \
                  'Please contact the system administrator. Additional error details are: %s' % response.content
        elif response.status_code == requests.codes.bad:
            # Bad Request
            msg = 'There is something wrong in the request. Please check all your inputs correctly.' \
                  'Additional error details are: %s' % response.content
        elif response.status_code == requests.codes.server_error:
            # Server Error occurred.
            msg = 'Some error has occurred on the server. Please try after some time!' \
                  'Additional error details are: %s' % response.content
        elif response.status_code == requests.codes.ok:
            # Successful
            success = True
            msg = 'Success'
            if response.headers.get('content-type') == 'application/json':
                # If the response is of type JSON, set the obj
                obj = response.json()

        return {'success': success, 'msg': msg, 'obj': obj}

    @staticmethod
    def handle_server_connection_error():
        '''
        This method handles the server connection error
        :return: A dictionary containing the failure flag and error message
        '''
        return {'success': False, 'msg': 'Cannot connect to Enhanced CWE system', 'obj': None}

   