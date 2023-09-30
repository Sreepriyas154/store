from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

# class Productsview(APIView):
#     def get(self,request,*args,**kwargs):
#         return Response({"msg":"inside the product"})
#
#
# class Addview(APIView):
#     def post(self,request,*args,**kwargs):
#         num1=request.data.get("num1")
#         num2=request.data.get("num2")
#         res=int(num1)+int(num2)
#         return Response({"msg":res})
# class Subview(APIView):
#     def post(self,request,*args,**kwargs):
#         num1=request.data.get("num1")
#         num2=request.data.get("num2")
#         res=int(num1)-int(num2)
#         return Response({"msg":res})
# class Multiview(APIView):
#     def post(self,reuest,*args,**kwargs):
#         num1 = request.data.get("num1")
#         num2 = request.data.get("num2")
#         res=int(num1)*int(num2)
#         return Response({"msg":res})
#
# class Divview(APIView):
#     def post(self,request,*args,**kwargs):
#         num1 = request.data.get("num1")
#         num2 =request.data.get("num2")
#         res=int(num1)/int(num2)
#         return Response({"msg":res})
#
class Cubeviwe(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=n**3
        return Response({"Result":res})

class Numchkview(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        if(n%2==0):
            res="number is even"
        else:
            res="number is odd"
        return Response(data=res)
class Factview(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        res=1
        for i in range(1,(n+1)):
            res=res*i
        return Response(data=res)

class Wordcountview(APIView):
    def post(self,request,*args,**kwargs):
        txt=request.data.get("txt")
        words=txt.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)
class Primenumview(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        f=0
        for i in range(1,n+1):
            if(n%i)==0:
                f=f+1
        if f==2:
            res="the number is prime"
        else:
            res="the number is not a prime"
        return Response(data=res)
class Palindromeview(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        rev=0
        m=n
        while n>0:
            rm=n%10
            rev=rev*10+rm
            n=n//10
        if m==rev:
            res="the number is plaindrome"
        else:
            res="not a palindome"
        return Response(data=res)

class Armstrongview(APIView):
    def post(self,request,*args,**kwargs):
        n=int(request.data.get("num"))
        rev=0
        m=n
        while n>0:
            rm=n%10
            rev=rev+rm*rm*rm
            n=n//10
        if m==rev:
            res="the number is armstrong "
        else:
            res="the number is not a armstrong"
        return Response(data=res)

