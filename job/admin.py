from django.contrib import admin

from .models import Jop , Category , ApplicantInfo

# Register your models here.
admin.site.register(Jop)
admin.site.register(Category)
admin.site.register(ApplicantInfo)
