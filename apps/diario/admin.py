from django.contrib import admin
from apps.diario.models import Registro, ListaAlimentos, AlimentosConsumidos, Pesagens,DadosPessoais

class ListandoRegistro(admin.ModelAdmin):
    list_display = ("id", "usuario", "data", "hora")
    list_display_links = ("id",)
    search_fields = ("usuario",)
    list_filter = ("usuario",)
    list_editable = ("usuario",)
    list_per_page = 10

class ListandoListaAlimentos(admin.ModelAdmin):
    list_display = ("id", "nome", "calorias_por_100g")
    list_display_links = ("id",)
    search_fields = ("id", "nome", "calorias_por_100g")
    list_filter = ("id", "nome", "calorias_por_100g")
    list_editable = ( "nome", "calorias_por_100g")
    list_per_page = 10

class ListandoAlimentosConsumidos(admin.ModelAdmin):
    list_display = ("id", "usuario", "registro", "alimento", "quantidade")
    list_display_links = ("id",)
    search_fields = ("id", "usuario", "registro", "alimento", "quantidade")
    list_filter = ("id", "usuario", "registro", "alimento", "quantidade")
    list_editable = ( "usuario", "registro", "alimento", "quantidade")
    list_per_page = 10

class ListandoPesagens(admin.ModelAdmin):
    list_display = ("id", "usuario", "registro", "peso")
    list_display_links = ("id",)
    search_fields = ("id", "usuario", "registro", "peso")
    list_filter = ("id", "usuario", "registro", "peso")
    list_editable = ("usuario", "registro", "peso")
    list_per_page = 10

class ListandoDadosPessoais(admin.ModelAdmin):
    list_display = ("id", "usuario", "altura", "data_nascimento")
    list_display_links = ("id",)
    search_fields = ("id", "usuario", "altura", "data_nascimento")
    list_filter = ("id", "usuario", "altura", "data_nascimento")
    list_editable = ("usuario", "altura", "data_nascimento")
    list_per_page = 10

# Register your models here.


admin.site.register(Registro, ListandoRegistro)
admin.site.register(ListaAlimentos, ListandoListaAlimentos)
admin.site.register(AlimentosConsumidos, ListandoAlimentosConsumidos)
admin.site.register(Pesagens, ListandoPesagens)
admin.site.register(DadosPessoais, ListandoDadosPessoais)