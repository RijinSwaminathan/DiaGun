from itertools import chain

from rest_framework import serializers

from products import models as model


class ViewCategorySerializer(serializers.Serializer):
    """Serializer class to view the list of category"""
    id = serializers.IntegerField()
    category_name = serializers.CharField()
    product = serializers.SerializerMethodField(default=None)

    def get_product(self, obj):
        """
        :param obj:
        :return: Get the product details according to category id
        """

        product_data = model.Product.objects.filter(category_id__parent_cat=obj.id)
        for i, c in enumerate(product_data):
            print(i, c, type(c))
            products = model.Product.objects.filter(category_id__parent_cat=c.category_id_id)
            product_qs = list(chain(product_data|products))
            product_ser = ViewShopProductSerializer(product_qs, many=True)
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
