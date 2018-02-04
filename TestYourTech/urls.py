"""TestYourTech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('action/run/', runView, name='run'),
    path('action/run_test/', runTestView.as_view()),
    path('actions/', ActionView.as_view()),
    path('action/<int:action_pk>/result/', action_result_list),
    path('action/<int:action_pk>/result/<int:result_pk>/', action_result_detail),
]
things = ['selector', 'testcase', 'result', 'action', 'action_link']
for x in things:
	urlpatterns += eval("[re_path(r'^%ss/$', %s_list),re_path(r'^%ss/(?P<pk>[0-9]+)/$', %s_detail)]" % (x, x, x, x))
