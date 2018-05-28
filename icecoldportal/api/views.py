from django.http import HttpResponse
# from django.shortcuts import render
# from django.contrib.auth.models import User, Group
# from rest_framework import viewsets
# from .serializers import BrotherSerializer
from .models import Brother


# Create your views here.


def healthcheck(request):
    return HttpResponse("The API is good to go", 200)


def get_all_brothers(request):
    queryset = Brother.objects.values()
    retset = []
    for brother in queryset:
        print(brother)
        retset.append(brother)
    return HttpResponse(queryset, 200)

# class BrotherViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows brothers to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-first_name')
#     serializer_class = BrotherSerializer
