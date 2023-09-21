from django.db import models
from django.contrib.auth.models import User


# создание сущности продукта
class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


# создание доступа к продукту
class AccessToProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    can_view = models.BooleanField(default=False)
    can_edit = models.BooleanField(default=False)


# создание урока
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    duration_seconds = models.IntegerField()
    products = models.ManyToManyField(Product, related_name='lessons')


# указание, что видео просмотрено
class LessonViewing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_viewed = models.BooleanField(default=False)

    def view_video(self):
        if self.end_time is not None:
            duration = (self.end_time - self.start_time).total_seconds()
            total_duration = self.lesson.duration_seconds
            if (duration / total_duration) >= 0.8:
                self.is_viewed = True
            else:
                self.is_viewed = False
        else:
            self.is_viewed = False

        self.save()
