from django.contrib import admin
import django.apps
# Register your models here.

models = django.apps.apps.get_models()

print(models)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass



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