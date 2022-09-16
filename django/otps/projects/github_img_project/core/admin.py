from django.contrib import admin

from core.models import Github

# Register your models here.


@admin.register(Github)
class GithubAdmin(admin.ModelAdmin):
    list_display = ['id', 'github_user', "image_link", "user"]
    