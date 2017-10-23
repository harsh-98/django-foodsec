#from django.contrib.auth.models import User, Group
from application.models import User, ColdStorage
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from application.serializers import UserSerializer, GroupSerializer, ColdStorageSerializer
import math as Math


@csrf_exempt
def userCreate(request):


    print(request)
    if request.method == 'GET':
        snippets = User.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def userLogin(request):


    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            snippet = User.objects.get(email = data['email'],password = data['password'])
        except User.DoesNotExist:
            return HttpResponse(status=404)
        serializer = UserSerializer(snippet)
        return JsonResponse(serializer.data)

#    elif request.method == 'PUT':
#        data = JSONParser().parse(request)
#        serializer = SnippetSerializer(snippet, data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data)
#        return JsonResponse(serializer.errors, status=400)#

#    elif request.method == 'DELETE':
#        snippet.delete()
#        return HttpResponse(status=204)

@csrf_exempt
def storeCreate(request):


    if request.method == 'GET':
        snippets = ColdStorage.objects.all()
        serializer = ColdStorageSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data['owner'])
        arr = data['yield']
        del data['yield']
        var = 1
        for i in arr:
           tmp = dict()
           tmp = dict()
           tmp['yieldType'] = i[0]
           tmp['space'] = i[1]
           tmp['empty'] = i[2]
           tmp1 = data.copy()
           tmp1.update(tmp)
           print(tmp1)

           serializer = ColdStorageSerializer(data=tmp1)
           if serializer.is_valid():
              serializer.save()
              var*=1
           else:
              var*=0
        if var == 1:
            return JsonResponse("created", status=201,safe=False)
        else :
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def nearColdStorage(request):


    if request.method == 'POST':
        data = JSONParser().parse(request)
        lon = data['longitude']
        lat = data['latitude']
        R = 6378
        radius = 50
        x1 = lon - Math.degrees(float(radius)/R/Math.cos(Math.radians(lat)))
        x2 = lon + Math.degrees(float(radius)/R/Math.cos(Math.radians(lat)))
        y1 = lat - Math.degrees(float(radius)/R)
        y2 = lat + Math.degrees(float(radius)/R)
        print(x1)
        print(x2)
        print(y1)
        print(y2)
        try:
            snippet = ColdStorage.objects.filter(longitude__gte = x1,
                                                 longitude__lte = x2, 
                                                 latitude__gte = y1, 
                                                 latitude__lte = y2,
                                                 empty__gte = data['quantity'],
                                                 yieldType = data['yieldType'])
            print(snippet)
        except ColdStorage.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ColdStorageSerializer(snippet, many=True)
        return JsonResponse(serializer.data, safe=False)