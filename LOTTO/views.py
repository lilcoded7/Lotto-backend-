from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from LOTTO.models.drawmodel import DrawnNumber
from LOTTO.models.machinemodel import MachineNumber
from .serializers import MachineSerializer, DrawNumerSerializer

# Create your views here.



class draw_number_view(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = DrawnNumber.objects.all()
    serializer_class = DrawNumerSerializer
    permission_classes = [AllowAny]


class machine_number_view(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin):
    queryset = MachineNumber.objects.all()
    serializer_class = MachineSerializer
    permission_classes = [AllowAny]
