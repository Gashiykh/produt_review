from django.contrib import admin
from webapp import models


admin.site.register(models.Product)

admin.site.register(models.Review)