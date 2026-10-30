from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .models import Course
from .permission import IsInstructorOrAdmin
from .serializers import CourseSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return 
class CreateCoursView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]  # noqa: RUF012
    permission_classes = [IsInstructorOrAdmin]  # noqa: RUF012
    
    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "Course created successfully!"}, 
            status = status.HTTP_201_CREATED
        )