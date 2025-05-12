from django.contrib import admin

from core.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'total_price', 'category','available')
    list_display_links = ('name',)
    list_editable = ('price', 'quantity',)
    search_fields = ('name',)
    actions = ('is_available','not_available')
    readonly_fields = ('created_at', 'updated_at')

    @admin.action(description="Make as is not available")
    def not_available(self,request, queryset):
        queryset.update(available=False)

    @admin.action(description="Make as available")
    def is_available(self,request,queryset):
        queryset.update(available=True)

    @admin.display(description="Total price")
    def total_price(self, obj):
        return obj.price * obj.quantity
