from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee,Node,Cityes
import csv
import os

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


if __name__ == '__main__':
    add_test_database()