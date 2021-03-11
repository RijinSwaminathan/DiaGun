from rest_framework import serializers

from products import models as model


class ViewCategorySerializer(serializers.Serializer):
    """Serializer class to view the list of category"""
    id = serializers.IntegerField()
    category_name = serializers.CharField()
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        """
        :param obj:
        :return: Get the product details according to category id
        """
        product_data = model.Product.objects.filter(category_id=obj.id)
        product_ser = ViewShopProductSerializer(product_data, many=True)
        return product_ser.data


class MediaSerializer(serializers.ModelSerializer):
    """Serializer to get the product image"""

    class Meta:
        model = model.Media
        fields = (
            'product_image',
        )


class ViewShopProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product_name = serializers.CharField()
    product_image = serializers.SerializerMethodField()

    def get_product_image(self, obj):
        """
        :param obj:
        :return: get the product image according to product id
        """
        if model.Media.objects.filter(product_id=obj.id).exists():
            image = model.Media.objects.get(product_id=obj.id)
            return image.product_image.name
        return None


class ViewShopSerializer(serializers.Serializer):
    """Serializer class to view the list of products"""
    data = serializers.SerializerMethodField()

    def get_data(self, obj):
        """
        :param obj:
        :return: get the category details according to shop_id
        """
        category_data = model.Category.objects.filter(shop_id=obj.id)
        category_ser = ViewCategorySerializer(category_data, many=True)
        return category_ser.data
