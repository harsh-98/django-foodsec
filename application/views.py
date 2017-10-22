#from django.contrib.auth.models import User, Group
from application.models import User
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from application.serializers import UserSerializer, GroupSerializer


#class UserViewSet(viewsets.ModelViewSet):
#        """
#            API endpoint that allows users to be viewed or edited.
#        """
#        queryset = User.objects.all().order_by('-date_joined')
#        serializer_class = UserSerializer#
#

#class GroupViewSet(viewsets.ModelViewSet):
#        """
#            API endpoint that allows groups to be viewed or edited.
#        """
#        queryset = Group.objects.all()
#        serializer_class = GroupSerializer


@csrf_exempt
def userCreate(request):
    """
    List all code snippets, or create a new snippet.
    """
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
def userLogin(request, pk):
    print(request)
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = User.objects.get(username = request.POST['username'],password = password.POST['password'])
    except User.DoesNotExist:
        return HttpResponse(status=404)
    print(snippet)
#    if request.method == 'GET':
#        serializer = SnippetSerializer(snippet)
#        return JsonResponse(serializer.data)#

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
