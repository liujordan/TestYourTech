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
    path('action/1/run', runView.as_view(), name='run'),
    # re_path(r'^selectors/$', selector_list, name='selector'),
    # re_path(r'^selectors/(?P<pk>[0-9]+)/$', selector_detail	),
    # re_path(r'^testcases/$', testcase_list, name='testcase'),
    # re_path(r'^testcases/(?P<pk>[0-9]+)/$', testcase_detail	),
]
things = ['selector', 'testcase', 'result', 'action']
for x in things:
	urlpatterns += eval("[re_path(r'^%ss/$', %s_list),re_path(r'^%ss/(?P<pk>[0-9]+)/$', %s_detail)]" % (x, x, x, x))
