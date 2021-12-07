from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from order.consumers.order_status_consumer import OrderStatusConsumer
from order.consumers.waiter_notifications_consumer import WaiterNotificationsConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('menu.urls')),
    path('api/', include('client_facility.urls')),
    path('api/', include('order.urls')),
]

websocket_urlpatterns = [
    url(r'^ws/waiter/notifications/(?P<waiter_id>[^/]+)/$', WaiterNotificationsConsumer.as_asgi()),
    url(r'^ws/order/notifications/(?P<order_id>[^/]+)/$', OrderStatusConsumer.as_asgi()),
]