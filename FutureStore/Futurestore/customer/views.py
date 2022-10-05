from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView,DeleteView,DetailView,ListView
from customer import forms
from django.urls import reverse_lazy
from owner.models import Product,Carts
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class RegistrationView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("login")

class LoginView(FormView):
    template_name = "login.html"
    form_class = forms.LoginForm
    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_products=Product.objects.all()
        context["products"]=all_products
        return context

class ProductDetailView(DetailView):
    template_name = "product-detail.html"
    model = Product
    context_object_name = "product"
    pk_url_kwarg = "id"

class AddToCartView(FormView):
    template_name = "add-to-cart.html"
    form_class = forms.CartForm

    def get(self,request,*args, **kwargs):
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"product":product})
    def post(self, request, *args, **kwargs):
        id=kwargs.get("id")
        product=Product.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(product=product,
                             user=user,
                             qty=qty)
        return redirect("home")
class MyCartView(ListView):
    model = Carts
    template_name = "cart-list.html"
    context_object_name = "carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user)



class CartRemoveview(ListView):
    model = Carts
    template_name = "cart-remove.html"
    context_object_name = "carts"

    def get_queryset(self):
        id=self.kwargs.get("id")
        cart=Carts.objects.get(id=id)
        cart.status="cancelled"
        cart.delete()
        messages.success(self.request,"removed successfully")
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-created_date")











# Create your views here.
