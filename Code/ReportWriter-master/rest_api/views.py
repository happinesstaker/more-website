import re
import json
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorld(APIView):
	def get(self, request):
		pass


	def post(self, request):
		
		print request.POST

		return Response(status=status.HTTP_200_OK)