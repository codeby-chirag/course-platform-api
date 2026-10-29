from django.urls import path

from .views import CreateCoursView

urlpatterns = [
    path('create/', CreateCoursView.as_view(), name='course-create'),
]