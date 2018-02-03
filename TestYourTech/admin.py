from django.contrib import admin
from .models import *

admin.site.register(Selector)
admin.site.register(TestCase)
admin.site.register(Result)

class ActionAdmin(admin.ModelAdmin):
	raw_id_fields = ("selector",)
admin.site.register(Action, ActionAdmin)