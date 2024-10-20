from django.contrib import admin
from django.urls import path
from .views import registration

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/registration/', registration)
]