from django.http import HttpResponse, JsonResponse
# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import detail_route, action, api_view
from rest_framework.response import Response
from .serializers import BrotherSerializer
from rest_framework.views import APIView

from .models import Brother

# Create your views here.





def healthcheck(request):
    """

    :param request:
    Description of parameter `request`: a Django request object that extends the HTTPRequest module
    in python. This will be the HTTP request that is sent from another server to our backend

    :return Response object:
    Description of return value: A response object that contains a descriptive string
    stating the api is healthy and a successful 200 status code
    """
    return Response(data="The API is good to go", status=200)


'''
Parameters
----------
request : an HTTP request object
    Description of parameter `request`: a Django request object that extends the HTTPRequest module in python. This will
    be the HTTP request that is sent from another server to our backend 

Return
---------
ret_value :  Response object
    Description of return value: A response object that contains a serialized response of all the current brothers in
    the api_brother table and a successful 200 status code
'''


@api_view(['GET'])  # Decorator that let's Django know to treat this function is meant to handle GET HTTP requests
def all_brothers(request):
    brothers = Brother.objects.all()
    serializer = BrotherSerializer(brothers, many=True)
    return Response(data=serializer.data, status=200)


'''
Parameters
----------
request : an HTTP request object
    Description of parameter `request`: a Django request object that extends the HTTPRequest module in python. This will
    be the HTTP request that is sent from another server to our backend 

Return
---------
ret_value :  Response object
    Description of return value: A successful 200 status code for the insertion of a new brother in the database
'''


@api_view(['POST'])  # Decorator that let's Django know to treat this function is meant to handle POST HTTP requests
def create_brother(request):
    requested_brother = request.data
    print(requested_brother['first_name'])
    new_brother = Brother(first_name=requested_brother['first_name'], last_name=requested_brother['last_name'],
                          crossing_date=requested_brother['crossing_date'], ship_name=requested_brother['ship_name'])
    new_brother.save()
    return Response(status=200)
