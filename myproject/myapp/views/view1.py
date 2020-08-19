from django.shortcuts import render
from django.http import HttpResponse
from myapp.models.students import Students
from myapp import models
# Create your views here.


def hello(request):
    res = Students.objects.all()
    # res=models.Students()
    # res.id = 1
    # res.name = "Aman Mishra"
    # res.email = "a@gmail.com"
    # res.save()
    # print("data is stored")
    # print(res.name)
    print(res[0].name)
    data = {"ID":res[0].id, "NAME": res[0].name, "EMAIL": res[0].email}
    # result = {"id": res[id], "name": res.name, "email": res.email}
    print(data)
    return HttpResponse(data["NAME"])
