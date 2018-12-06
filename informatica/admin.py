from django.contrib import admin
from .models import Author, Genre, Book, BookInstance
# Register your models here.

#admin.site.register(Author)
class BookInline(admin.TabularInline):
    model=Book

class AuthorAdmin(admin.ModelAdmin):
    list_display=('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields=('first_name', 'last_name',('date_of_birth', 'date_of_death'))
    inlines=[BookInline]
admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(BookInstance)

class BooksInstanceInline(admin.TabularInline):
    model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'display_genre')
    inlines=[BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display=('book', 'status', 'due_back','id')
    list_filter=('book','status', 'due_back','id')

    fieldsets=(
        (None, {
            'fields':('book', 'imprint', 'id')
        }),
        ('Abailavility',{
            'fields':('status', 'due_back')
        }),
    )
admin.site.register(Genre)