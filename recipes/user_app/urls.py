from django.contrib import admin
from django.urls import path
from .views import registration
# from .views import CustomLoginView

app_name = 'user_app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/registration/', registration),
    # path('login/', CustomLoginView.as_view(), name='login'),
]