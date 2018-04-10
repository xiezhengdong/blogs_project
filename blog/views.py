from django.shortcuts import render,HttpResponse

# Create your views here.

class yewu(object):

    def login(self,req):
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            print(user,password)
            return render(req, 'login.html')
        return render(req,'login.html')

    def register(self,req):
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            password_1 = req.POST['password1']
            print(user,password,password_1)
            return render(req, 'register.html')
        return render(req, 'register.html')
