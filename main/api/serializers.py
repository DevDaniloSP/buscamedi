from rest_framework import serializers
from main import models

class MedicamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Medicamento
        fields = '__all__'
        