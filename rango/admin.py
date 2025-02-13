from django.contrib import admin
from rango.models import Category, Page
from rango.models import UserProfile

# Customize the Category admin to prepopulate the slug field automatically.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Register the models with the admin site.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(UserProfile)
