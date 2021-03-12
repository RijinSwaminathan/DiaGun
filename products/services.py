from DiaGun import response as message
from products.models import Category
from products.serializers import ViewCategorySerializer


class ProductManagementService:
    """ service layer """

    def get_product_by_shop(self, shop_id):
        shop_data = Category.objects.filter(shop_id=shop_id)
        if shop_data:
            shop_ser = ViewCategorySerializer(shop_data, many=True)
            return message.fetch_data_response(data=shop_ser.data)
        return message.not_found()
