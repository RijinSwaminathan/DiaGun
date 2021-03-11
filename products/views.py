# Create your views here.
from rest_framework.views import APIView

from DiaGun.response import exception_response
from products.services import ProductManagementService

product_management_service = ProductManagementService()


class ProductView(APIView):
    def get(self, request, pk):
        """
        :param request:
        :param pk:
        :return: list down the product details according to the shop id
        """
        try:
            return product_management_service.get_product_by_shop(shop_id=pk)
        except Exception as error:
            return exception_response(error)
