from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view

from .views import *
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v2',
        description="Description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="progavanlav@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=(),  # Отключите глобальную аутентификацию здесь, если нужно
)

router = routers.DefaultRouter()
router.register(r'organizations', OrganizationsViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'categoryPayment', CategoryPaymentViewSet)
router.register(r'insurance_cases', InsuranceCasesViewSet)
router.register(r'insurance_cotracts', InsuranceCotractsViewSet)
router.register(r'insurance_agents', InsuranceAgentsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('doc/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')

]