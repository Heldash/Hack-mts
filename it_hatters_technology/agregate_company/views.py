import json

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView,status
from drf_spectacular.utils import extend_schema
from .models import Employee,Node,Cityes
from .serializers import EmployeeSerializer,NodeSerializer,CitySerializer,EmployeeSerializerAll
import csv

def add_test_database(request):
    nodes = {}
    cityes = {}
    with open("agregate_company/shtat.csv","r",encoding="utf-8") as file:
        csvReader = csv.reader(file)
        fields = next(csvReader)
        for row in csvReader:
            address = []
            for i in range(0,5):
                if row[i] !="" and row[i] not in nodes:
                    if Node.objects.filter(name=row[i]).exists():
                        node = Node.objects.get(name = row[i])
                        nodes[row[i]] = node.id
                        address.append(str(node.id))
                    else:
                        node = Node(name=row[i],type=fields[i])
                        node.save()
                        nodes[row[i]]=node.id
                        address.append(str(nodes[row[i]]))
                elif row[i] !="" and row[i] in nodes:
                    address.append(str(nodes[row[i]]))
            role = row[6]
            position = row[5]
            first_name = row[8]
            last_name = row[7]
            phone_number = row[9]
            print(address)
            if row[10] in cityes:
                city = cityes[row[10]]
            else:
                if Cityes.objects.filter(name = row[11]).exists():
                    cit = Cityes.objects.get(name = row[11])
                    cityes[row[10]] = cit.id
                    city = cit.id
                else:
                    cit = Cityes(name = row[10])
                    cit.save()
                    cityes[row[10]]=cit.id
                    city = cit.id
            addr = row[11]
            email = None
            if row[12] != "":
                email = row[12]
            if not(Employee.objects.filter(phone_number=phone_number).exists()):
                worker = Employee(first_name=first_name,last_name=last_name,role=role,position=position,
                                  phone_number = phone_number,email = email,path = ".".join(address),address =addr,
                                  location = cit)
                worker.save()
    return HttpResponse("succes")


class AllUsers(APIView):
    @extend_schema(summary="Получить всех сотрудников",
                   description="Вместе с сотрудниками на выходе получаешь id локаций и номера узлов дерева"
                   )
    def get(self,request):
        users = EmployeeSerializer(Employee.objects.select_related("location","location").all(),many=True)
        nodes = NodeSerializer(Node.objects.all(),many=True)
        cityes = CitySerializer(Cityes.objects.all(),many=True)
        print(users.data)
        print(nodes.data)
        return Response({"employers":users.data,
                         "nodes_id":nodes.data,
                         "city_id":cityes.data})
        # cityes = Node.objects.all()
class GetUserById(APIView):
    def get(self,request,user_id):
        try:
            worker = Employee.objects.get(id=user_id)
        except Employee.DoesNotExist:
            return Response("Error",status=status.HTTP_404_NOT_FOUND)
        worker = EmployeeSerializerAll(worker)
        return Response(worker,status=status.HTTP_200_OK)
class EditUserFName(APIView):
    def post(self,request:Request):
        id = request.POST.get("id",None)
