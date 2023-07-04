from rest_framework import viewsets, generics, status

from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def calculate_sum(request):
    # Получение параметров из URL
    param1 = int(request.GET.get('param1', 0))
    param2 = int(request.GET.get('param2', 0))
    param3 = int(request.GET.get('param3', 0))

    # Вычисление суммы
    total_sum = param1 + param2 + param3

    # Создание словаря с результатами
    data = {
        'param1': param1,
        'param2': param2,
        'param3': param3,
        'total_sum': total_sum
    }

    # Возврат API с результатами
    return Response(data)


class ListProductSerializer:
    pass


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)


class OrderDetailCreateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)


class CompanyCreateView(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class CompanyDetailCreateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)


class FeedbackListView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = (IsAuthenticated,)


class FeedbackCreateView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (IsAuthenticated,)

class DeliveryDocsViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDocs.objects.all()
    serializer_class = DeliveryDocsSerializer


class AllViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {
            'delivery_docs': DeliveryDocsSerializer(DeliveryDocs.objects.all(), many=True).data,
            'deliveries': DeliverySerializer(Delivery.objects.all(), many=True).data,
            'drivers': DriverSerializer(Driver.objects.all(), many=True).data,
            'prices': PriceSerializer(Price.objects.all(), many=True).data,
            'driver_documents': DriverDocumentSerializer(DriverDocument.objects.all(), many=True).data,
            'orders': OrderSerializer(Order.objects.all(), many=True).data,
            'users': UserSerializer(User.objects.all(), many=True).data,
            'feedback': FeedbackSerializer(Feedback.objects.all(), many=True).data,
            'company': CompanySerializer(Company.objects.all(), many=True).data,
            'messages': MessageSerializer(Message.objects.all(), many=True).data,
            'message_docs': MessageDocSerializer(MessageDoc.objects.all(), many=True).data,
            'company_feedback': CompanyFeedbackSerializer(CompanyFeedback.objects.all(), many=True).data,
            'feedback_images': FeedbackImageSerializer(FeedbackImage.objects.all(), many=True).data,
            'chats': ChatSerializer(Chat.objects.all(), many=True).data,
        }
        return Response(data)


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class DriverDocumentViewSet(viewsets.ModelViewSet):
    queryset = DriverDocument.objects.all()
    serializer_class = DriverDocumentSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageDocViewSet(viewsets.ModelViewSet):
    queryset = MessageDoc.objects.all()
    serializer_class = MessageDocSerializer


class CompanyFeedbackViewSet(viewsets.ModelViewSet):
    queryset = CompanyFeedback.objects.all()
    serializer_class = CompanyFeedbackSerializer


class FeedbackImageViewSet(viewsets.ModelViewSet):
    queryset = FeedbackImage.objects.all()
    serializer_class = FeedbackImageSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
