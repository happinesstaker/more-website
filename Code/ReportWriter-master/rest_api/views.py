import re
import json
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from report.models import *

class ModificationAdvice(APIView):
    PARAM_RID = "id"
    PARAM_TITLE = "title"
    PARAM_CONTENT = "content"

    @staticmethod
    def _check_all_sections_present(data_dict):
        sections_missing = []
        if ModificationAdvice.PARAM_RID not in data_dict:
            sections_missing.append(ModificationAdvice.PARAM_RID)
        if ModificationAdvice.PARAM_TITLE not in data_dict:
            sections_missing.append(ModificationAdvice.PARAM_TITLE)
        if ModificationAdvice.PARAM_CONTENT not in data_dict:
            sections_missing.append(ModificationAdvice.PARAM_CONTENT)

        return sections_missing

    @staticmethod
    def _form_err_msg_section_missing(sections_missing):
        return ("The following sections should be provided but missing: " +
                ("".join(section+", " for section in sections_missing)).rstrip(", "))

    @staticmethod
    def _form_err_msg_method_not_allowed():
        return "Use POST method for this REST API function."

    def get(self, request):
        # Because all the other REST API functions are implemented using GET,
        # we return an error message that tells the developer to use the POST method.
        return Response(data=self._form_err_msg_method_not_allowed(), status=status.HTTP_405_METHOD_NOT_ALLOWED)


    def post(self, request):
        sections_missing = self._check_all_sections_present(request.data)
        # Now if sections_missing is not empty, we return the error.
        if len(sections_missing)>0:
            err_msg = self._form_err_msg_section_missing(sections_missing)
            return Response(data=err_msg, status=status.HTTP_400_BAD_REQUEST)
        # print request.POST
        rid = request.data[self.PARAM_RID]
        title = request.data[self.PARAM_TITLE]
        content = request.data[self.PARAM_CONTENT]
        report_list = Report.objects.filter(rid=rid)

        if not report_list:
            err_msg = "Orginal Report containing this muo has been removed."
            return Response(data=err_msg, status=status.HTTP_400_BAD_REQUEST)

        report = report_list[0]
        print report
        advice = Advice(report=report,advice_title=title,advice_text=content)
        advice.save()
        report.promoted = False
        report.custom = 'custom'
        report.save()

        return Response(status=status.HTTP_200_OK)







