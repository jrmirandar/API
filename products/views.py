from products.models import Product, Category

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from products.serializers import ProductSerializer, CategorySerializer

class ProductViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  lookup_field = 'int_code'

  def create(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.add_product')):
      return Response({'detail': 'User has no permissions to add products'}, status.HTTP_401_UNAUTHORIZED)
    
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)

  def update(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.change_product')):
      return Response({'detail': 'User has no permissions to change products'}, status.HTTP_401_UNAUTHORIZED)
    
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
      instance._prefetched_objects_cache = {}

    return Response(serializer.data)

  def destroy(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.delete_product')):
      return Response({'detail': 'User has no permissions to delete products'}, status.HTTP_401_UNAUTHORIZED)

    instance = self.get_object()
    instance.active =(True, False)[instance.active]
    
    serializer = self.get_serializer(instance, data={'active': instance.active}, partial=True)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    return Response(serializer.data)

class CategoryViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  lookup_field = 'name'

  def create(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.add_category')):
      return Response({'detail': 'User has no permissions to add categories'}, status.HTTP_401_UNAUTHORIZED)
    
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)
    return Response(serializer.data, headers=headers, status=status.HTTP_201_CREATED)

  def update(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.change_category')):
      return Response({'detail': 'User has no permissions to change categories'}, status.HTTP_401_UNAUTHORIZED)
    
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
      instance._prefetched_objects_cache = {}

    return Response(serializer.data)

  def destroy(self, request, *args, **kwargs):
    if(not request.user.has_perm('products.delete_category')):
      return Response({"detail": "User has no permission to delete category"}, status.HTTP_401_UNAUTHORIZED)
    instance = self.get_object()
    instance.active = (True, False)[instance.active] 
    serializer = self.get_serializer(instance, data={'active': instance.active}, partial=True)
    serializer.is_valid(raise_exception=True)
    
    self.perform_update(serializer)
    return Response(serializer.data)


