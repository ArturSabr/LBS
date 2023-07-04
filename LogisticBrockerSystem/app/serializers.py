from rest_framework import serializers
from .models import DeliveryDocs, Delivery, Driver, Price, DriverDocument, Order, User, Feedback, Company, Message, MessageDoc, CompanyFeedback, FeedbackImage, Chat


class ListOrderSerializer(serializers.Serializer):
    orders = serializers.JSONField()

    def create(self, validated_data):
        for i in validated_data['orders']:
            print(i)
        return {'Привет': 'Привет'}




class DeliveryDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDocs
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class DriverDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverDocument
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'


class MessageDocSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageDoc
        fields = '__all__'


class CompanyFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFeedback
        fields = '__all__'


class FeedbackImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackImage
        fields = '__all__'


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'
