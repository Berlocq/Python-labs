from django.contrib import admin

# Register your models here.
from . import models 

class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'book_name'
    ]
class GenreAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'Author',
        'style',
        'description'
    ]

admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Author, AuthorAdmin)

