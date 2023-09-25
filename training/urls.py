from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('lessons/', views.LessonListView.as_view(), name='List of lessons'),
    path('lessons/<int:product_id>/', views.ProductLessonList.as_view(), name='Each lesson'),
    # path('statistics/', views.ProductStatistics.as_view(), name='Stat')

]
