from django.contrib import admin
from .models import *

admin.site.register(Selector)
admin.site.register(TestCase)
admin.site.register(Result)
admin.site.register(Action)