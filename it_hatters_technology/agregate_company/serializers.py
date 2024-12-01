from rest_framework import serializers
from .models import Employee,Cityes,Node

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id","first_name","last_name","path","phone_number","location","address","role",
                  "position"]
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cityes
        fields = "__all__"
class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = "__all__"
class EmployeeSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"