from django.urls import path
from apps.diario.views import index,login

urlpatterns = [
    ##Pagina base
    path('', index, name='index'),
    ##Login
    path('login/',login, name='login')
]

