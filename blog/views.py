from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect,JsonResponse
from blog.models import zhuce
import json
# Create your views here.

class yewu(object):

    def login(self,req):
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            print(user,password)
            date = zhuce.objects.all()
            d = date.values()[0]
            mylist =['用户名不存在']
            if user not in d.values():
                return render(req,'login.html',{'tishi':json.dumps(mylist)})
            else:
                return HttpResponseRedirect('http://127.0.0.1/index/')
        return render(req,'login.html')

    def register(self,req):#用户注册

        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            password_1 = req.POST['password1']
            #print(user,password,password_1)
            date = zhuce.objects.create(user=user,password=password)
            date.save()
            return render(req, 'register.html')
        return render(req, 'register.html')

    def index(self,req):
        return render(req,'index.html')
