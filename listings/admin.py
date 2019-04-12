from django.contrib import admin
from listings.models import Listing

class listingAdmin(admin.ModelAdmin):
    list_display = ('id','title','isPublished','realtor')
    list_display_links = ('id','title')
    search_fields = ('title','address','realtor','city','price')
    list_filter = ('realtor',)
    list_editable = ('isPublished',)
    list_per_page = 25 

    def get_ordering(self, request):
        return ['id']
admin.site.register(Listing,listingAdmin)