from django.contrib import admin



from .models import Username

# Register your models here.



@admin.register(Username)
class UsernameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')