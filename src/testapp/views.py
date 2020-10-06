from django.shortcuts import render
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from testapp.models import Test
from testapp.serializers import TestSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.


# class EmployeeCRUDCBV(View):
#     def get(self, request, *args, **kwargs):
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pdata = JSONParser().parse(stream)
#         id = pdata.get('id', None)
#         if id is not None:
#             tData = Test.objects.get(id= id)
#             serializer = TestSerializer(emp)
#             json_data = JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data, content_type = 'application/json')

#         qs = Test.objects.all()
#         serializer = TestSerializer(qs, many = True)
#         json_data = JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data, content_type='application/json')

    # def post(self, request, *args, **kwargs):
    #     json_data = request.body
    #     print('json_data: ',json_data)

    #     #converting json data into python data
    #     stream = io.BytesIO(json_data)
    #     pdata = JSONParser().parse(stream)


    #     #converting python data in data base model instance
    #     serializer = TestSerializer(data = pdata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         msg = {'msg': 'Resource created successfully'}
    #         json_data = JSONRenderer().render(msg)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json', status=400)

# @api_view(('GET','POST',))
# def articleList(request):

#     if request.method == 'GET':
#         articles = Test.objects.all()
#         serializer = TestSerializer(articles, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TestSerializer(data=data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)


class ArticleList(APIView):

    "Listing of the data --- get method"
    def get(self,request,format=None):
        test = Test.objects.all()
        serializer = TestSerializer(test,many=True)
        return Response(serializer.data)

    "Post data"

    def post(self,request,format=None):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            return Response({
                "id":instance.id,
                "testdata":instance.testData
            },status=201)