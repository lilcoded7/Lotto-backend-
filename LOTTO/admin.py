from django.contrib import admin
from LOTTO.models.drawmodel import DrawnNumber
from LOTTO.models.machinemodel import MachineNumber

# Register your models here.

admin.site.register(DrawnNumber)
admin.site.register(MachineNumber)