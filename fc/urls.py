"""fc URL Configuration

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
from django.urls import path,  re_path
from django.conf.urls import url
from invent import views

from invent.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('invent/', index),
    url(r'^$', views.index,name='home'),
    url(r'^about/$', views.about,name='about'),
    url(r'^get_name/', views.get_name,name='get name'),
    url(r'^parts/$',views.inventory_parts_table),
    re_path(r'^parts/details/(?P<id>\d+)/$',views.inventory_parts_form),
    re_path(r'^parts/details/$',views.inventory_parts_form),
    re_path(r'^customer/details/(?P<id>\d+)/$',views.customer_form),
    re_path(r'^customer/details/$',views.customer_form),
    url(r'^customer/$', views.customer_overview_table),
    
]
