from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import LessonViewing, Lesson, Product, AccessToProduct
from .serializers import LessonViewingSerializer, LessonSerializer, ProductSerializer


class LessonListView(generics.ListAPIView):
    serializer_class = LessonViewingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Lesson.objects.filter(title=user)
        return queryset


class ProductLessonList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        owner = self.request.user
        product_id = self.kwargs['product_id']
        return Product.objects.filter(owner_id=product_id, owner=self.request.user)


# @api_view(['GET'])
# def product_statistics(request):
#     products = Product.objects.all()
#     data = []
#     for product in products:
#         viewed_lessons_count = lesson_statuses.count()
#         viewed_time = lesson_statuses.aggregate(sum=Sum('viewed_time'))['sum'] or 0
#         users_count = AccessToProduct.objects.filter(product=product).count()
#         purchases = round(AccessToProduct.objects.filter(product=product).count() / User.objects.count()) * 100, 2)
#
#         product_data = {
#             'product_name': product.name,
#             'viewed_lessons_count': viewed_lessons_count,
#             'viewed_time': viewed_time,
#             'users_count': users_count,
#             'purchases': purchases
#         }
#         data.append(product_data)
#
#     return Response(data)


def index(request):
    return HttpResponse("ZDAROVA!")
