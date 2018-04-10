from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect
# Create your views here.

class yewu(object):

    def login(self,req):
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            print(user,password)
            return HttpResponseRedirect('http://127.0.0.1/index/')
        return render(req,'login.html')

    def register(self,req):
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            password_1 = req.POST['password1']
            print(user,password,password_1)
            return render(req, 'register.html')
        return render(req, 'register.html')

    def index(self,req):
        return render(req,'index.html')
