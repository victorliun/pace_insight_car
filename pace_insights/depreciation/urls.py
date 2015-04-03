from django.conf.urls import url, include
from rest_framework import routers
 
from depreciation import views, api_views
 
 
router = routers.DefaultRouter()
# register job endpoint in the router
router.register(r'jobs', api_views.JobViewSet)
router.register(r'carmakes', api_views.CarMakeViewSet)
router.register(r'carmodels', api_views.CarModelViewSet)
router.register(r'carversions', api_views.CarVersionViewSet)
router.register(r'depreciations', api_views.DepreciationViewSet)
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/test-json', views.test_json),
]