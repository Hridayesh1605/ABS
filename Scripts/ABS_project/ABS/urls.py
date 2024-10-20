"""
URL configuration for ABS_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home,name="home"),
    # path('login',v.login),
    # path('register',v.register.as_view()),
    # path('add',v.addUser.as_view())
    path('register',v.signup),
    path('login',v.signIn,name="logIn"),
    # path('pieChart',v.chart),
    path('admin',v.admin),
    path('user_list',v.ulist),
    path('staff_list',v.slist),
    path('delete/<int:id1>',v.delete),
    path('deleteb/<int:id1>',v.deleteb),
    # path('edit/<int:id1>',v.edit),
    path('edit/<int:pk>',v.editUser.as_view()),
    path('userHome',v.uHome),
    path('signOut',v.signOut),
    path('staffRegister',v.s_reg),
    path('staff_home',v.staffH),
    path('addExtraUserDet',v.addExtraUserDet),
    path('viewUDet',v.viewUDet),
    path('ambRegister',v.a_reg),
    path('book/<int:id3>',v.book),
    path('ambulanceCard',v.AmbulanceCard),
    path('message_after_book',v.message_after_book),
    path('delete_rides/<int:id3>',v.delete_rides),
    path('accept_ride/<int:id4>',v.accept_ride),
    path('finish_ride/<int:id5>',v.finish_ride),
    path('checkout/<int:id6>',v.checkout)
    
    
]
