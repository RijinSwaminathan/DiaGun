# Register your models here.
from django.contrib import admin

from products import models as model

# register Shop with admin panel
admin.site.register(model.Shop)
# register Category model with admin panel
admin.site.register(model.Category)
# register Product model with admin panel
admin.site.register(model.Product)
# register Media model with admin panel
admin.site.register(model.Media)
