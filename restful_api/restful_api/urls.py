from django.urls import path, include
from django.contrib import admin
from address import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('users.urls'))
]

