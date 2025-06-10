from django.contrib import admin
from fm.models import forms

class form_admin(admin.ModelAdmin):
    list_display = ('user_name','user_email','user_phone','user_message')

admin.site.register(forms,form_admin)

# Register your models here.
