from django.contrib import admin
from .models import Teacher, URL

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['icerikanabaslik', 'derece', 'sinif', 'onayli_mi']
    actions = ['make_approved']

    def onayli_mi(self, obj):
        return obj.onayli
    onayli_mi.boolean = True
    onayli_mi.short_description = 'Onaylı mı?'

    def make_approved(self, request, queryset):
        queryset.update(onayli=True)
    make_approved.short_description = "Seçilen öğeleri onayla"

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['onayli']
        return []

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(URL)

