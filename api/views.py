from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Books,Reviews
from api.serializers import BookSerialzers,ReviewSerializer
from rest_framework.viewsets import ViewSet,ModelViewSet
from api.serializers import Userserializer
from django.contrib.auth.models import User
from rest_framework import authentication,permissions
from  rest_framework.decorators import action
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
# class Cubeviwe(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         res=n**3
#         return Response({"Result":res})
#
# class Numchkview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         if(n%2==0):
#             res="number is even"
#         else:
#             res="number is odd"
#         return Response(data=res)
# class Factview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         res=1
#         for i in range(1,(n+1)):
#             res=res*i
#         return Response(data=res)
#
# class Wordcountview(APIView):
#     def post(self,request,*args,**kwargs):
#         txt=request.data.get("txt")
#         words=txt.split(" ")
#         wc={}
#         for w in words:
#             if w in wc:
#                 wc[w]+=1
#             else:
#                 wc[w]=1
#         return Response(data=wc)
# class Primenumview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         f=0
#         for i in range(1,n+1):
#             if(n%i)==0:
#                 f=f+1
#         if f==2:
#             res="the number is prime"
#         else:
#             res="the number is not a prime"
#         return Response(data=res)
# class Palindromeview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         rev=0
#         m=n
#         while n>0:
#             rm=n%10
#             rev=rev*10+rm
#             n=n//10
#         if m==rev:
#             res="the number is plaindrome"
#         else:
#             res="not a palindome"
#         return Response(data=res)
#
# class Armstrongview(APIView):
#     def post(self,request,*args,**kwargs):
#         n=int(request.data.get("num"))
#         rev=0
#         m=n
#         while n>0:
#             rm=n%10
#             rev=rev+rm*rm*rm
#             n=n//10
#         if m==rev:
#             res="the number is armstrong "
#         else:
#             res="the number is not a armstrong"
#         return Response(data=res)

class Productsview(APIView):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerialzers(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        # bname=request.data.get("name")
        # bauthor=request.data.get("author")
        # bprice=int(request.data.get("price"))
        # bpublication=request.data.get("publication")
        # bqty=int(request.data.get("qty"))
        # Books.objects.create(name=bname,author=bauthor,price=bprice,publication=bpublication,qty=bqty)
        serializer=BookSerialzers(data=request.data)
        if serializer.is_valid():
            Books.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return  Response(data=serializer.errors)


class Productdetailview(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        serializer=BookSerialzers(book,many=False)#deserializaion
        return  Response(data=serializer.data)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Books.objects.get(id=id).delete()
        return Response(data="deleted")
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        serializer=BookSerialzers(data=request.data)
        if serializer.is_valid():
            Books.objects.filter(id=id).update(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


#model serializer use
class Reviewsview(APIView):
    def get(self,request,*args,**kwargs):
        reviews=Reviews.objects.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data==serializer.errors)

class Reviewdetailsview(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(qs,many=False)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=Reviews.objects.get(id=id)
        serializer=ReviewSerializer(instance=qs,data=request.data)#modelserializer step
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Reviews.objects.get(id=id).delete()
        return Response(data="deleted")



class Productsviewsetview(ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def list(self,request,*args,**kwargs):
        qs=Books.objects.all()
        serializer=BookSerialzers(qs,many=True)
        return Response(data=serializer.data)
    def create(self,request,*args,**kwargs):
        serializer=BookSerialzers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        serializer=BookSerialzers(qs,many=False)
        return Response(data=serializer.data)
    def update(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Books.objects.get(id=id)
        serializer=BookSerialzers(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        return Response(data=="deleted")


class Productmodelviewsetview(ModelViewSet):
    serializer_class = BookSerialzers
    queryset = Books.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        user=request.user
        Reviews.objects.create(book=qs,user=user,comment=request.data.get("comment"),rating=request.data.get("rating"))
        return Response(data="created")
    @action(methods=["get"],detail=True)
    def get_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        reviews=qs.reviews_set.all()
        serializer=ReviewSerializer(reviews,many=True)
        return Response(data=serializer.data)
    @action(method=["post"],detail=True)
    def




class Reviewmodelviewsetview(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Reviews.objects.all()
    def list(self, request, *args, **kwargs):
        all_reviews=Reviews.objects.all()
        if 'user' in request.query_params:
            all_reviews=all_reviews.filter(user=request.query_params.get("user"))
        serializer=ReviewSerializer(all_reviews,many=True)
        return Response(data=serializer.data)

class Usersview(ModelViewSet):
    serializer_class = Userserializer
    queryset = User.objects.all()
