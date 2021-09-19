from django.contrib import admin

# Register your models here.
from .models import (Pays,Ville,Marques,Employés)

admin.site.register(Pays)
admin.site.register(Ville)
admin.site.register(Marques)
admin.site.register(Employés)