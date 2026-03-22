from django.contrib import admin
from .models import chaiVerity, chaiReview, store, chaiCertification

# Register your models here.
class chaiReviewInLine(admin.TabularInline):
    model = chaiReview
    extra = 2

class chaiVerityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [chaiReviewInLine]

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_verities')

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number')


admin.site.register(chaiVerity, chaiVerityAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(chaiCertification, chaiCertificateAdmin)



