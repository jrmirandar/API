from django.urls import path
from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from products.views import ProductViewSet, CategoryViewSet
from customers.views import CustomersViewSet, ContactsViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register('product', ProductViewSet)
router.register('product/category', CategoryViewSet)
router.register('customer', CustomersViewSet)
router.register('customer/contact', ContactsViewSet)

app_name = 'api'

urlpatterns = router.urls