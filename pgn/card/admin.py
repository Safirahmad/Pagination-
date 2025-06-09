from django.contrib import admin
from card.models import card
from card.models import newcar
class card_admin(admin.ModelAdmin):
    list_display = ('car_title' ,'car_desc','car_line')

class new_card_admin(admin.ModelAdmin):
    
    list_display = ('car_new_title','car_new_des')

admin.site.register(card,card_admin)
admin.site.register(newcar,new_card_admin)
# Register your models here.
