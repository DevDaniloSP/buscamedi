from rest_framework import viewsets
from main.api import serializers
from django_filters import rest_framework as filters
from main.models import Medicamento


class MedicamentoFilter(filters.FilterSet):

    class Meta:
        model = Medicamento
        fields = {
            'nome' : ['contains'],
            'local': ['contains' ],
        }



class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = serializers.MedicamentoSerializers
    filterset_class = MedicamentoFilter

 
    



