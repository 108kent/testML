from django.contrib import admin
from .models import Data

# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'age', 'year_in_germany', 'predictions')


admin.site.register(Data, DataAdmin)