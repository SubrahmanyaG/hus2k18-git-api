"""git_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import pprint

from django.conf.urls import url
from django.contrib import admin
from django.http import JsonResponse

import json

def get_api(request):
    res = {
        "total_count": 30,
        "items": [],
        "incomplete_results": False
    }
    with open('git_api/data.json') as f:
        data = json.load(f)
        res['items'] = data
    return JsonResponse(res)


urlpatterns = [
    url(r'^core/', get_api),
]