from django.contrib import admin

from main.models import Medicamento


@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display=Medicamento.CampoBusca
    search_fields=Medicamento.Busca
    list_filter= Medicamento.FiltraCampos

