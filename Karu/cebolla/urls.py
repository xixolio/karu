from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from cebolla import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'paymentType',views.PaymentTypeViewSet)
router.register(r'ingredientType',views.IngredientTypeViewSet)
#router.register(r'local',views.LocalViewSet)
router.register(r'ingredient',views.IngredientViewSet)
#router.register(r'ingredientLocal',views.IngredientLocalViewSet)
#router.register(r'entry',views.EntryViewSet)
#router.register(r'discharge',views.DischargeViewSet)
router.register(r'purchase',views.PurchaseViewSet)
router.register(r'order',views.OrderViewSet)
router.register(r'item',views.ItemViewSet)
#router.register(r'user',views.UserViewSet)

urlpatterns = [
#    url(r'^ingredientType/$', views.IngredientTypeList.as_view()),
#    url(r'^ingredientType/(?P<pk>[0-9]+)/$', views.IngredientTypeDetail.as_view()),
#    url(r'^paymentType/$', views.PaymentTypeList.as_view()),
#    url(r'^paymentType/(?P<pk>[0-9]+)/$', views.PaymentTypeDetail.as_view()),
    url(r'^', include(router.urls)),
#    url(r'^ingredient/$', views.IngredientList.as_view()),
#   url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view()),
#    url(r'^local/$', views.LocalList.as_view()),
#    url(r'^local/(?P<pk>[0-9]+)/$', views.LocalDetail.as_view()),
#    url(r'^ingredientLocal/$', views.IngredientLocalList.as_view()),
#    url(r'^ingredientLocal/(?P<pk>[0-9]+)/$', views.IngredientLocalDetail.as_view()),
]

#urlpatterns = format_suffix_patterns(urlpatterns)