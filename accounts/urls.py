from django.urls import path

from .views import LoginView, SignUpView

urlpatterns = [
    path('register/', SignUpView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login')
]


