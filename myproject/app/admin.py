from django.contrib import admin
import django.apps
from .models import Post, Profile
from django import  forms
# Register your models here.

models = django.apps.apps.get_models()

# print(models)

# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass



# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', ('author', 'slug')]


# class PostAdmin(admin.ModelAdmin):
#     TEXT = 'Some description text'
#     fieldsets = (
#         ('Section 1', {
#             'fields': ('title', 'author'),
#             'description': '%s' % TEXT,
#         }),
#         ('Section 2', {
#             'fields': ('slug',),
#         }),
#     )

# admin.site.register(Post, PostAdmin)



# class PostForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         self.fields['title'].help_text = 'New Help Text'

#     class Meta:
#         model = Post
#         exclude = ('',)

# class PostFormAdmin(admin.ModelAdmin):
#     form = PostForm

# admin.site.register(Post, PostFormAdmin)

class Filter(admin.ModelAdmin):
    list_display = ('id', 'email', 'created_at', 'role', 'is_active')
    list_filter = ('is_active', 'role', 'created_at')

admin.site.register(Profile, Filter)