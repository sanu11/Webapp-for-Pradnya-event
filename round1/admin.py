from django.contrib import admin
from .models import Junior, Senior, jquestions, squestions

# Register your models here.
admin.site.register(Junior)
admin.site.register(Senior)
admin.site.register(jquestions)
admin.site.register(squestions)