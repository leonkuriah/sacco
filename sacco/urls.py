"""sacco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin

from members.views import ListMembers
from members.views import AddMembers
from members.views import EditMembers
from members.views import DeleteMembers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListMembers.as_view(), name='list_members'),
    path('new', AddMembers.as_view(), name='members_form'),
    path('edit/<int:pk>', EditMembers.as_view(), name='members_edit'),
    path('delete/<int:pk>', DeleteMembers.as_view(), name='members_delete'),
]
