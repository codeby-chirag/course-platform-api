from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['instructor', 'course_title', 'category', 'description', 'duration', 'enrollment_start_date', 'enrollment_end_date', 'course_start_date', 'course_end_date']  # noqa: RUF012
        read_only_fields = ['instructor']  # noqa: RUF012

    def validate_course_title(self, value):
        if Course.objects.filter(course_title__iexact = value).exists():
            raise serializers.ValidationError("A Course with this title is already exist.")
        return value
    