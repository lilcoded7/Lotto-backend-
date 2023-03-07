from rest_framework import serializers 
from LOTTO.models.drawmodel import DrawnNumber
from LOTTO.models.machinemodel import MachineNumber


class DrawNumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DrawnNumber
        fields = ['monday','tuesday','wednesday','thursday','friday'] 


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineNumber
        fields = ['monday','tuesday','wednesday','thursday','friday'] 
