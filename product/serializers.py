from rest_framework import serializers
from .models import Products

class ProductsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Products
        fields = '__all__'

        def create(self, validated_data):
            return Products.objects.create(**validated_data)

        def update_product(self,instance, validated_data):
            instance.product_name = validated_data('product_name','product_name'),
            instance.product_description = validated_data('product_description','product_description'),
            instance.product_image_1 = validated_data('product_image_1','product_image_1'),
            instance.product_image_2 = validated_data('product_image_2','product_image_2'),
            instance.product_image_3 = validated_data('product_image_3','product_image_3'),
            instance.product_category = validated_data('product_category','product_category'),
            instance.product_amount = validated_data('product_amount','product_amount'),
            instance.available_location = validated_data('available_location','available_location'),
            instance.date_posted = validated_data('date_posted','date_posted')
            instance.save()
            return instance