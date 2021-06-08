from rest_framework import routers
from .api import OrderViewSet, MachineViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register('orders', OrderViewSet, 'orders')
router.register('machines', MachineViewSet, 'machines')
router.register('clients', ClientViewSet, 'clients')


urlpatterns = router.urls
