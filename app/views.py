import hashlib
import random
from django.core.cache import cache

import time
from django.shortcuts import render, redirect

#首页
from app.models import User, Goods


def index(request):
    # token = request.session.get('token')
    # userid = cache.get(token)
    # response_data ={
    #     'user': None
    # }
    # if userid:
    #     user = User.objects.get(pk=userid)
    #     response_data['user'] = user
    #
    #     orders = user.order_set.all()
    #     # 待付款
    #     response_data['waitpay'] = orders.filter(status=0).count()
    #     # 待发货
    #     response_data['paydone'] = orders.filter(status=1).count()
    # # 获取
    token = request.session.get('token')
    userid = cache.get(token)
    goods_list = Goods.objects.all()

    response_data = {
        'user':userid,
        'goods_list':goods_list
    }
    user = None
    if token:
        user = User.objects.get(pk=userid)




    return render(request, 'index.html', context=response_data)

#登录
def login(request):

    return render(request, 'login.html')


#加秘
def generate_password(param):
    md5 = hashlib.md5()
    md5.update(param.encode('utf-8'))
    return md5.hexdigest()
#获取tonen
def generate_token():
    temp = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(temp.encode('utf-8'))
    return md5.hexdigest()

#注册
def register(request):

    # 获取数据
    if request.method =='GET':
        return render(request,'register.html')
    elif request.method =='POST':
        phone = request.POST.get('phone')
        name = request.POST.get('name')
        password = generate_password(request.POST.get('password'))

        # 存入数据库
        user = User()
        user.name = name
        user.password = password
        user.phone = phone
        user.save()

        # 状态保持
        token = generate_token()
        cache.set(token, user.id, 60*60*24*3)
        request.session['token'] = token
        return redirect('app:index')


def logout(request):
    request.session.flush()

    return redirect('app:index')

# 商品详情
def detail(request,productid):
    return render(request,'detail.html')