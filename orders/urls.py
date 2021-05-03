from rest_framework import routers
from .api import OrderViewSet, MachineViewSet, ClientViewSet

router = routers.DefaultRouter()
router.register('api/orders', OrderViewSet, 'orders')
router.register('api/machines', MachineViewSet, 'machines')
router.register('api/clients', ClientViewSet, 'clients')


urlpatterns = router.urls
