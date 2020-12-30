from django.contrib import admin
# after creating model we need to register here in admin to see it
from .models import Week



# this class will enable us to see the creation date from
# our model as a read only
class WeekAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)



admin.site.register(Week, WeekAdmin)
