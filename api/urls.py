from django.urls import path
from api.views import RegistroView, VehiculoViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views.admin_temp import crear_admin


vehiculo_list = VehiculoViewSet.as_view({
    'get': 'list',      
    'post': 'create'    
})

vehiculo_detail = VehiculoViewSet.as_view({
    'get': 'retrieve',  
    'put': 'update',    
    'delete': 'destroy'
})

urlpatterns = [
    # Endpoints de Autenticación
    path('auth/register/', RegistroView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoints del CRUD de Vehículos
    path('vehiculos/', vehiculo_list, name='vehiculo-list'),
    path('vehiculos/<int:pk>/', vehiculo_detail, name='vehiculo-detail'),
    
    path('crear-admin/', crear_admin, name='crear-admin'),
]