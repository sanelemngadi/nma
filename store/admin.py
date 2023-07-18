from django.contrib import admin
from store import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Filter)
admin.site.register(models.FAQ)
admin.site.register(models.NMAPageSettings)
admin.site.register(models.Product)
admin.site.register(models.ProductImageVariant)
admin.site.register(models.ProductReview)
