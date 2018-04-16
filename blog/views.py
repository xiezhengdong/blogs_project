from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponseRedirect,JsonResponse
from blog.models import zhuce
from blog import models
from django.forms.models import model_to_dict
import json
import time,base64
# Create your views here.

class yewu(object):

    def login(self,req):#用户登录
        global date_oj
        if req.method =="POST":
            user = req.POST['user']#获取用户名
            password = req.POST['password']#获取密码
            print(user,password)
            date_oj = models.zhuce.objects.get(user=user)#查询数据里的用户名
            print(date_oj.user)
            mylist =['用户名不存在']
            if user in  date_oj.user:
                return redirect('/blog/index/')
            else:
                return render(req, 'login.html', {'tishi': json.dumps(mylist)})
        return render(req,'login.html')

    def register(self,req):#用户注册
        if req.method =="POST":
            user = req.POST['user']
            password = req.POST['password']
            password_1 = req.POST['password1']
            #print(user,password,password_1)
            date = models.zhuce.objects.create(user=user,password=password)
            date.save()
            return JsonResponse({'status':'succes','content':'注册成功'})
        return render(req, 'register.html')

    def cook_login(self,req):#实验cookies登录
        if req.method=="POST":
            name = req.POST.get('user')
            pwd = req.POST.get('pwd')
            if name=='root' and pwd=='123':
                res = redirect('/blog/cook_index/')
                res.set_cookie('username',name)
                res.set_cookie("_utm",int(time.time()))
                return res
        return render(req,'cookies.html')

    def cook_index(self,req):#实验cookies登录
        if req.COOKIES.get('username') and req.COOKIES.get('_utm'):
            name = req.COOKIES.get('username')
            utm = req.COOKIES.get('_utm')
            return render(req,'cookies_index.html')
        else:
            return  redirect('/blog/cook_login/')
        return  render(req,'cookies_index.html')


    def index(self,req):#博客首页
        return render(req,'index.html')

    def liuyan(self,req):#留言板
        return render(req,'liuyan.html')

