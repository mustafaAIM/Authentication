from django.urls import path
from .views import Register
from .views import CustomTokenObtainPairView

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]