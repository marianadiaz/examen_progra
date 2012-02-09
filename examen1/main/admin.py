from django.contrib import admin
from main.models import Author, Article, Comment, Label


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'birth_date',)
	search_fields = ('last_name',)


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('author', 'title',)
	search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


class LabelAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Label, LabelAdmin)
