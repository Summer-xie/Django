# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
import random
from datetime import datetime
from RedbagModel.models import Redbag
# Create your views here.
def add(request,a,b):
        #a=request.GET.get('a',0)
        #b=request.GET.get('b',0)
        c=int(a)+int(b)
        return HttpResponse(str(c))
        #return HttpResponse("Hello world ! ")

def index(request):
        return render(request,'index.html')

def redbag(request):
        return render(request,'redbag.html')

def is_chinese(uchar):
        #判断一个unicode是否是汉字
        if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
                return True
        else:
                return False

def is_number(uchar):
        #判断一个unicode是否是数字
        if uchar >= u'\u0030' and uchar<=u'\u0039':
                return True
        else:
                return False
def is_other(uchar):
        #判断是否非汉字，数字和英文字符
        if not (is_chinese(uchar) or is_number(uchar) or is_alphabet(uchar)):
                return True

        else:
                return False
def is_rightfloat(num):
        #判断小数位<=2
        string=str(num)
        if string.find('.')>=1 and string.find('.')>=len(string)-3:
                return True
        else:
                return False
def test(request):
        number=request.POST.get('number')
        money=request.POST.get('money')
        n=''
        m=''
        lst=[]
        lst2=[]
        dit={}
        tips=''
        total=0
        if number and money:
                #if is_number(number) and is_number(money):
                n=str(number.encode("utf-8"))
                m=str(money.encode("utf-8"))
                #r=Regbag(num='1',money='4.5',datetime='2016-3-10 15:34:09')
                #r.save()
                if n.isdigit() and n!='0' and n!=0:
                        n=int(n)
                        if n<0 or n>100:
                                tips='红包个数不能超过100！'
                                return render(request,'redbag.html',{'result':dit,'tips':tips})
                        maxofm=int(n)*200
                        minofm=int(n)*0.01
                        if is_number(money) and ((m.isdigit() and m!='0') or is_rightfloat(m)):
                                m=float(m)
                                total=m
                                if m>0 and minofm<=m<=maxofm:
                                        if m==n*200.0 or n==1 or m==n*0.01:
                                                print m,n
                                                for i in range(1,n+1):
                                                        lst.append(('%.2f')%(m/n))
                                                        lst2.append(i)
                                                        b=('%.2f')%(m/n)
                                        else:
                                                lastRed,lst2,lst=randomRed(m,n)
                                                while lastRed>200:
                                                        lastRed,lst2,lst=randomRed(m,n)
                                                lst2.append(n)
                                                lst.append(('%.2f')%lastRed)

                                        dit=dict(zip(lst2,lst))
                                        for key,value in dit.items():
                                                regbag1=Redbag(number=n,total=total,xuhao=key,single=value)
                                                regbag1.save()
                                elif m>maxofm:
                                        tips='单个红包金额不能超过200元！'
                                elif m<minofm:
                                        tips='单个红包金额不能少于0.01元！'
                                #tips=('number:%d money:%.2f')%(n,m)
                        else:
                                tips='红包个数或总金额输入不正确！请重新输入'
                else:
                        tips='红包个数或总金额输入不正确！请重新输入'
        elif number==''  or money=='':
                tips='输入不能为空！'
        return render(request,'redbag.html',{'result':dit,'tips':tips,'num':n,'money':money,'datetime':str(datetime.now())[:19]})

def randomRed(m,n):
        m=float(m)
        lst=[]
        lst2=[]
        dit={}
        for i in range(1,n):
                while True:
                        #print i
                        a=round(random.uniform(0.01,(m-(n-i)*0.01)/(n-i)),2)
                        #print a
                        if a!=0 and a<=200:
                                m-=a
                                lst.append(('%.2f')%a)
                                b=('%.2f')%a
                                lst2.append(i)
                                time=str(datetime.now())[:19]
                                #regbag1=Redbag(number=n,total=total,xuhao=i,single=b,datetime=time)
                                #regbag1.save()
                                break
        return m,lst2,lst

