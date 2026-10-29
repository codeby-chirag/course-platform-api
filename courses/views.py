from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Course
from .serializers import CourseSerializer
from .permission import IsInstructorOrAdmin


class CreateCoursView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsInstructorOrAdmin]  # noqa: RUF012
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the instructor
        serializer.save(instructor=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        self.perform_create(serializer)
        
        return Response(
            {"message": "Course created successfully!"}, 
            status = status.HTTP_201_CREATED
        )
        
        
        