from DiaGun import response as message
from products.models import Shop
from products.serializers import ViewShopSerializer


class ProductManagementService:
    """ service layer """

    def get_product_by_shop(self, shop_id):
        shop_data = Shop.objects.get(id=shop_id)
        if shop_data:
            shop_ser = ViewShopSerializer(shop_data)
            return message.fetch_data_response(data=shop_ser.data)
        return message.not_found()
