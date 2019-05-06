"""wingtel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from wingtel.att_subscriptions.views import ATTSubscriptionViewSet
from wingtel.plans.views import PlanViewSet
from wingtel.purchases.views import PurchaseViewSet
from wingtel.sprint_subscriptions.views import SprintSubscriptionViewSet

router = routers.DefaultRouter()

router.register(r'att_subscriptions', ATTSubscriptionViewSet, base_name='att_subscriptions')
router.register(r'plans', PlanViewSet, base_name='plans')
router.register(r'purchases', PurchaseViewSet, base_name='purchase')
router.register(r'sprint_subscriptions', SprintSubscriptionViewSet, base_name='sprint_subscriptions')

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include((router.urls, 'api'), namespace='api')),
]