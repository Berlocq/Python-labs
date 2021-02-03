from django.contrib import admin

# Register your models here.
from . import models 

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'book_name'
    ]
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'style',
        'description'
    ]


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Genre, GenreAdmin)
