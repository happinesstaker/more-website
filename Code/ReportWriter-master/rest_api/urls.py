from django.conf.urls import url
from rest_api import views

urlpatterns = [
    url(r'^report_feedback/test$', views.HelloWorld.as_view(), name="restapi_CustomMUO_Create"),
]
