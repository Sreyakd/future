"""dishes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dishapi.views import DishesView,DishDetailView,DishModelView,DishDetailsModelView,DishViewSetView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("api/v3/dishes",DishViewSetView,basename="dishes")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myd/dishes',DishesView.as_view()),
    path('myd/dishes/<int:id>',DishDetailView.as_view()),
    path('api/v2/myd/dishes',DishModelView.as_view()),
    path('api/v2/myd/dishes/<int:id>',DishDetailsModelView.as_view())
]+router.urls
