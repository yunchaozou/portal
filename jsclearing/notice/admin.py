from django.contrib import admin
from jsclearing.notice.models import Category,Story

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    model=Category
    prepopulated_fields = {'slug': ('label',)}
admin.site.register(Category, CategoryAdmin)

class StoryAdmin(admin.ModelAdmin):
    model=Story
    list_display = ('title', 'category','owner', 'status', 'created', 'modified','is_top')
    search_fields = ('title', 'html_content')
    list_filter = ('status', 'owner', 'created', 'modified','is_top')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Story, StoryAdmin)