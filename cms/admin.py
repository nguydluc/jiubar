from django.contrib import admin
from .models import Category, Item, Contact, TimeSet, OperationHour, Gallery


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = ("name", "description")
    list_per_page = 20


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("phone", "address", "email", "facebook_link", "instagram_link")


@admin.register(TimeSet)
class TimeSetAdmin(admin.ModelAdmin):
    list_display = ("opening", "closing")


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image", "description")
    exclude = ("image_url",)

    def image_url(self, obj):
        return obj.image_url

    image_url.short_description = "Image URL"


@admin.register(OperationHour)
class OperationHourAdmin(admin.ModelAdmin):
    pass
