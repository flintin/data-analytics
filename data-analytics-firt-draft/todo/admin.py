from django.contrib import admin
from django.db import models

from .models import ToDo, Author,Book,Publisher,Store
from markdownx.widgets import AdminMarkdownxWidget

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ["title", "user"]
    list_filter = ["user"]
    search_fields = ["title", "user"]

    class Meta:
        model = ToDo

#***********************************************

class AuthorDisplay(admin.ModelAdmin):
	list_display = ['name']

class BookDisplay(admin.ModelAdmin):
	list_display = ['bookname']

class PubDisplay(admin.ModelAdmin):
	list_display = ['pubname']

class StoreDisplay(admin.ModelAdmin):
	list_display = ['storename']

admin.site.register(ToDo, MyModelAdmin)
admin.site.register(Author, AuthorDisplay)
admin.site.register(Book, BookDisplay)
admin.site.register(Publisher, PubDisplay)
admin.site.register(Store, StoreDisplay)