"""firstpro URL Configuration

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
from greetings import views
from blogapi import views as bview

from calculator import views as cview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goodmorning/',views.GoodmorningView.as_view()),
    path('goodafternoon/',views.GoodAfternoonView.as_view()),
    path('goodevening/',views.GoodEveningView.as_view()),
    path('greetings/',views.GreetingsView.as_view()),
    path('operations/add/',cview.AddView.as_view()),
    path('operations/sub/',cview.SubView.as_view()),
    path('operations/mul/',cview.MulipleView.as_view()),
    path('operations/cube/',cview.CubeView.as_view()),
    path('operations/fact/',cview.FactorialView.as_view()),
    path('operations/word/',cview.WordCountView.as_view()),
    path('social/posts/',bview.PostsView.as_view()),
    path('social/posts/<int:pid>',bview.PostDetailsView.as_view())




    ]
