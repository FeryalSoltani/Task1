import re
from django.core.validators import RegexValidator
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


phone_regx = re.compile(r'''^(\d{2,4})-?(\d*)$''', re.VERBOSE)


class PhoneValidator(RegexValidator):
    regex = phone_regx
    message = ('Invalid Phone Number')



class sampleThrottlins(APIView):
    throttle_classes = (UserRateThrottle,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)
