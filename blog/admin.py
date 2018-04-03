from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['title']}),
		('Content', {'fields':['author','text']}),
		('Date Info', {'fields':['create_date', 'publish_date'], 'classes':['collapse']}),
	]
	list_display = ('title','create_date','author')
	list_filter = ['create_date']
	search_fields = ['title']

admin.site.register(Post, PostAdmin)
