from django.contrib import admin
from .models import Leyend
# Register your models here.

class LeyendAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

admin.site.register(Leyend, LeyendAdmin)