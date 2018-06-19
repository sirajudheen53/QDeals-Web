from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Deal, WishList, Purchase, ItemImage, Category, Vendor

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = '__all__'

class DealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deal
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class WishListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    deal = DealSerializer()

    class Meta:
        model = WishList
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    deal = DealSerializer()

    class Meta:
        model = Purchase
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class DealsListSerilaizer(serializers.ModelSerializer):
    vendor = VendorSerializer()
    category = CategorySerializer()
    class Meta:
        model = Deal
        fields = '__all__'

