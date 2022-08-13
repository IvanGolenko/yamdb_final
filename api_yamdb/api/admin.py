from django.contrib import admin
from users.models import User
from reviews.models import Category, Title, Genre


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'category']


admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(User)
