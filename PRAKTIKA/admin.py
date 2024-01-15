from .models import *
# Register your models here.
from django.contrib import admin

# Register your models here.
@admin.register(Poln_text)
class Poln_textAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')

@admin.register(Exhibition_tema)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
@admin.register(Exh_nov_iz)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
@admin.register(Kontakt)
class KontaktAdmin(admin.ModelAdmin):
    list_display = ( 'dol', 'name')
@admin.register(Date)
class DateAdmin(admin.ModelAdmin):
    list_display = ('dat', 'title')
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass
#admin.site.register(Tags)




