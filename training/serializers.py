from rest_framework import serializers
from .models import LessonViewing, Product, AccessToProduct, Lesson


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'owner')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonViewingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViewing
        fields = ('lesson', 'is_viewed', 'start_time', 'end_time')


class LessonInfoSerializer(serializers.ModelSerializer):
    lesson = serializers.CharField()
    status = serializers.BooleanField()
    timestamp = serializers.IntegerField()