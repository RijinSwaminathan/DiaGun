from rest_framework import serializers

from products import models as model


class ViewCategoryNameSerializer(serializers.Serializer):
    category_name = serializers.CharField()


class ViewCategorySerializer(serializers.Serializer):
    """Serializer class to view the list of category"""
    id = serializers.IntegerField()
    category_name = serializers.SerializerMethodField()

    product = serializers.SerializerMethodField()

    def get_category_name(self, obj):
        category_name = model.Category.objects.filter(parent_cat=obj.id)
        if category_name:
            return obj.category_name
        return obj.category_name

    def get_product(self, obj):
        """
        :param obj:
        :return: Get the product details according to category id
        """
        category_name = model.Category.objects.filter(parent_cat=obj.id)

        if category_name:
            for i in range(len(category_name)):
                product_data = model.Product.objects.filter(
                    category_id__category_name__contains=category_name[i])
                product_ser = ViewShopProductSerializer(product_data, many=True)
                return product_ser.data
        products = model.Product.objects.filter(category_id=obj.id)
        product_ser = ViewShopProductSerializer(products, many=True)
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
