from django.conf.urls import url
from rest_api import views

urlpatterns = [
    url(r'^report_feedback$', views.ModificationAdvice.as_view(), name="restapi_ModificationAdvice"),
]
