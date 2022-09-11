from rest_framework import serializers

from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'icon_image')


class Subscription0(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['choice']


class SubscriptionSerializer(serializers.ModelSerializer):
    Subscription = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('title', 'from_price', 'image', 'subcategory', 'Subscription')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'from_price', 'image', 'subscription')


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'from_price', 'image', 'subcategory', 'date_created')


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'image', 'from_price', 'subcategory')


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'title', 'category')


# Добавления постов
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('post', 'image')


class AddPostSerializer(serializers.ModelSerializer):
    # Image_Post = ImageSerializer(many=True, read_only=True)  # Вложенный Сериализатор
    Image_Post = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('id', 'category', 'subcategory',
                  'title', 'from_price', 'to_price',
                  'description', 'Image_Post', 'city',
                  'email', 'phone_number','views'
                  )


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model =Views
        fields ='__all__'