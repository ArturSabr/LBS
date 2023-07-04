from rest_framework.routers import DefaultRouter
from django.conf import settings
from .views import *
from django.urls import path
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'all', AllViewSet, basename='all')
router.register(r'deliverydocs', DeliveryDocsViewSet)
router.register(r'delivery', DeliveryViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'price', PriceViewSet)
router.register(r'driverdocument', DriverDocumentViewSet)
router.register(r'order', OrderViewSet)
router.register(r'user', UserViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'message', MessageViewSet)
router.register(r'messagedoc', MessageDocViewSet)
router.register(r'companyfeedback', CompanyFeedbackViewSet)
router.register(r'feedbackimage', FeedbackImageViewSet)
router.register(r'chat', ChatViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('order/list', OrderListView.as_view()),
    path('order/create', OrderCreateView.as_view()),
    path('order/<int:pk>', OrderDetailCreateDeleteView.as_view()),
    path('company/list', CompanyListView.as_view()),
    path('company/create', CompanyCreateView.as_view()),
    path('company/<int:pk>', CompanyDetailCreateDeleteView.as_view()),
    path('feedaback/list', FeedbackListView.as_view()),
    path('feedaback/create', FeedbackCreateView.as_view()),
    path('calculate/', calculate_sum, name='calculate-sum'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
