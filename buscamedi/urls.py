from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from main.api import viewsets as medicamentoviewsets

route = routers.DefaultRouter()

route.register(r'main', medicamentoviewsets.MedicamentoViewSet, basename="Medicamentos")





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
