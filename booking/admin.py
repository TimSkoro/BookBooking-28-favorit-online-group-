from django.contrib import admin

from booking.models import Book, Category, Author, Employer


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'changed_date', 'slug')
    readonly_fields = ('created_date', 'changed_date', 'slug')


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('user', 'boss_name', 'slaves_count', 'changed_count')
    readonly_fields = ('slaves_count',)


admin.site.register(Category)
admin.site.register(Author)
# admin.site.register(Employer)
