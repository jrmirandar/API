from customers.models import Customer, Contact

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from customers.serializers import ContactSerializer, CustomerSerializer


class CustomersViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    Lookup_field = "nit"

    def create(self, request, *args, **kwargs):
        if(not request.user.has_perm('customers.add_customer')):
            return Response({"detail": "User has no permission to add product"}, status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        if (not request.user.has_perm('customers.change_customer')):
            return Response({"detail": "User has no permission to change product"}, status.HTTP_401_UNAUTHORIZED)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if(not request.user.has_perm('customers.delete_customer')):
            return Response({"detail": "User has no permission to delete product"}, status.HTTP_401_UNAUTHORIZED)
        instance = self.get_object()
        instance.active = (True, False)[instance.active] 
        serializer = self.get_serializer(instance, data={'active': instance.active}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ContactsViewSet(CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, GenericViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    Lookup_field = "name"

    def create(self, request, *args, **kwargs):
        if(not request.user.has_perm('customers.add_contact')):
            return Response({"detail": "User has no permission to add product"}, status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        if (not request.user.has_perm('customers.change_contact')):
            return Response({"detail": "User has no permission to change product"}, status.HTTP_401_UNAUTHORIZED)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        if(not request.user.has_perm('customers.delete_contact')):
            return Response({"detail": "User has no permission to delete product"}, status.HTTP_401_UNAUTHORIZED)
        instance = self.get_object()
        instance.active = (True, False)[instance.active] 
        serializer = self.get_serializer(instance, data={'active': instance.active}, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)