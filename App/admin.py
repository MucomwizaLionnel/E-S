from django.contrib import admin

from .models import *
from .models import User

# Register your models here.


admin.site.register(Techniciens)
admin.site.register(Tache)
admin.site.register(Equipe)
admin.site.register(Stock)
admin.site.register(Produit)
