from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.http import FileResponse
from django.core.paginator import Paginator, EmptyPage
from blog.models import zhuce, UserMssge
from blog import models
from django.forms.models import model_to_dict
import json
import time

# Create your views here.


class yewu(object):

    def login(self, req):  # 用户登录
        global date_oj
        if req.method == "POST":
            print(888888888888888888888888)
            user = req.POST['user']  # 获取用户名
            password = req.POST['password']  # 获取密码
            print(user, password)
            date_oj = models.zhuce.objects.get(user=user)  # 查询数据里的用户名
            v = models.zhuce.objects.all()

            # print(v)
            print(date_oj.user)
            mylist = ['用户名不存在']
            if user in date_oj.user:
                return redirect('/blog/index/')
            else:
                return render(req, 'login.html', {'tishi': json.dumps(mylist)})
        return render(req, 'login.html')

    def register(self, req):  # 用户注册
        if req.method == "POST":
            user = req.POST['user']
            password = req.POST['password']
            password_1 = req.POST['password1']
            # print(user,password,password_1)
            date = models.zhuce.objects.create(user=user, password=password)
            date.save()
            return JsonResponse({'status': 'succes', 'content': '注册成功'})
        return render(req, 'register.html')

    def cook_login(self, req):  # 实验cookies登录
        if req.method == "POST":
            name = req.POST.get('user')
            pwd = req.POST.get('pwd')
            if name == 'root' and pwd == '123':
                res = redirect('/blog/cook_index/')
                res.set_cookie('username', name)
                res.set_cookie("_utm", int(time.time()))
                return res
        return render(req, 'cookies.html')

    def cook_index(self, req):  # 实验cookies登录
        if req.COOKIES.get('username') and req.COOKIES.get('_utm'):
            name = req.COOKIES.get('username')
            utm = req.COOKIES.get('_utm')
            return render(req, 'cookies_index.html')
        else:
            return redirect('/blog/cook_login/')
        # return  render(req,'cookies_index.html')

    def index(self, req):  # 博客首页
        return render(req, 'index.html')

    def liuyan(self, req):  # 留言板
        return render(req, 'liuyan.html')

    def python(self, req):  # python文章首页
        return render(req, 'py.html')

    def django(self, req):  # django文章首页
        return render(req, 'dj.html')

    def test_html(self, req):  # 测试HTML的样式
        return render(req, '样式.html')

    def content(self, request, id=''):  # 文章详情页
        user_id = id
        if request.method == 'GET':
            artice = models.artice.objects.filter(id=id)
            message = UserMssge.objects.all().values()  # 查出所有评论内容
            content_artice = artice.values()[0]['content']
            edmit_time = artice.values()[0]['shjian']
            title = artice.values()[0]['title']
            return render(request,
                          'content.html',
                          {'content_artice': content_artice,
                           'time': edmit_time,
                           'title': title,
                           'message': message})
        # elif request.method == 'POST':
        #     comment = request.POST.get('comment')
        #     author = request.POST.get('author')
        #     UserMssge.objects.create(author=author, content=comment)
        #     redirect('blog/python/content/'+ str(user_id) + '/')

    def user_message(self, request):
        if request.method == "POST":
            comment = request.POST.get('comment')
            author = request.POST.get('author')
            print(comment)
            UserMssge.objects.create(author=author, content=comment)
            info = {'name':author,'content':comment}
            return HttpResponse(json.dumps(info))
        return render(request,'content.html')

    def about_author(self, request):
        return render(request, 'about.html')

    def display_data(self, request):  # 可视化数据
        return render(request, 'tubiao.html')

    def page_py(self, req):  # python文章分页
        global skum
        sum = models.artice.objects.all().values()
        print(sum)
        pageintor = Paginator(sum, 3)
        num = req.GET.get('num')
        try:
            skum = pageintor.page(num)
        except Exception as e:
            print(e)
        print(num)
        page = '/blog/python/page/?num='
        shang_page = page + str(int(num) - 1)
        xia_page = page + str(int(num) + 1)
        return render(
            req, 'py.html', {
                'skum': skum, 'sp': shang_page, 'xp': xia_page, 'num': num})

    def page_dj(self, req):  # django文章分页
        global skum
        sum = models.artice.objects.all().values()
        print(sum)
        pageintor = Paginator(sum, 3)
        num = req.GET.get('num')
        try:
            skum = pageintor.page(num)
        except Exception as e:
            print(e)
        print(num)
        page = '/blog/django/page/?num='
        shang_page = page + str(int(num) - 1)
        xia_page = page + str(int(num) + 1)
        return render(
            req, 'dj.html', {
                'skum': skum, 'sp': shang_page, 'xp': xia_page, 'num': num})

    def upload(self, request):  # 上传文件
        if request.method == 'GET':
            #path = '/static/images/timg.jpg'
            return render(request, 'upload.html')
        elif request.method == 'POST':
            import os
            user = request.POST.get('user')
            print(user)
            fa = request.POST.get('fa')
            obj = request.FILES.get('fa')
            print(obj.name, obj.size)
            f = open(
                os.path.join(
                    'D:\\blogs_project\\blog\\static\\images\\' +
                    obj.name),
                'wb')
            for i in obj.chunks():
                f.write(i)
            f.close()
           # return render(request, 'upload.html')
            return redirect('/blog/upload')

    def download(self, request):  # 下载文件

        start_nginx = 'sudo /etc/init.d/nginx start'

        d = 'http://nginx.org/download/nginx-1.12.2.tar.gz'
        import os
        file = open(
            os.path.join(
                'D:\\blogs_project\\blog\\static\\css',
                'app.css'),
            'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="app.css"'
        return response
