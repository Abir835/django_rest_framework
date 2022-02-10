from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from myapp.models import Contact
from myapp.serializers import ContactSerializer


@csrf_exempt
def myapi(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        contact_list = Contact.objects.all()
        serializer = ContactSerializer(contact_list, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        contact_list = ContactSerializer(data=data)
        if contact_list.is_valid():
            contact_list.save()
            return JsonResponse(contact_list.data, status=201)
        return JsonResponse(contact_list.errors, status=400)


@csrf_exempt
def update_api(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        con_update = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ContactSerializer(con_update)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ContactSerializer(con_update, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        con_update.delete()
        return HttpResponse(status=204)

