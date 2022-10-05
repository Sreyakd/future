from django.shortcuts import render,redirect
from django.views.generic import View
from todoapp import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from todoapp.models import Todos

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=forms.RegistrationForm()
        return render(request,"registration.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("signin")
        else:
            return render(request, "registration.html",{"form":form})

        # print(request.POST.get("firstname"))
        # print(request.POST.get("lastname"))

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form = forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)


                print("login success")
                return redirect("index")
            else:
                print("invalid credientials")

        # print(request.POST.get("username"))
        # print(request.POST.get("password"))
        return render(request, "login.html",{"form":form})


class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")

class TodoAddView(View):
    def get(self,request,*args,**kwargs):
        form=forms.TodoForm()
        return render(request,"add-todo.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.TodoForm(request.POST)
        if form.is_valid():
            form.instance.user=request.user
            form.save()

            return redirect("index")

        else:
            return render(request, "add-todo.html", {"form": form})

class TodoListView(View):
    def get(self,request,*args,**kwargs):
        all_todos=Todos.objects.filter(user=request.user)
        return render(request,"todolist.html",{"todos":all_todos})


def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    Todos.objects.get(id=id).delete()
    return redirect("todolist")

class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        return render(request,"tododetail.html",{"todo":todo})





# Create your views here.
