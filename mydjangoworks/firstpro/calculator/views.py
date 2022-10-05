from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

class AddView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1+n2
        return Response({"msg":res})
class SubView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1-n2
        return Response({"msg":res})
class MulipleView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        n2=request.data.get("num2")
        res=n1*n2
        return Response({"msg":res})

class CubeView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n1=request.data.get("num1")
        res=n1**3
        return Response({"msg":res})

class FactorialView(APIView):
    def post(self,request,*args,**kwargs):
        print(request.data)
        n=request.data.get("num1")
        i=1
        f=1
        while(i<=n):
            f=f*i
            i+=1
        return Response({"msg":f})

class WordCountView(APIView):
    def post(self,request,*args,**kwargs):
        text=request.data.get("text")
        words=text.split(" ")
        wc={}
        for w in words:
            if w in wc:
                wc[w]+=1
            else:
                wc[w]=1
        return Response(data=wc)