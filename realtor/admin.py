from django.contrib import admin
from realtor.models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    list_display_linkes = ('id','name')
    search_fields = ('name','email')
    list_per_page = 25

    def get_ordering(self, request):
        return ['name']
admin.site.register(Realtor,RealtorAdmin)