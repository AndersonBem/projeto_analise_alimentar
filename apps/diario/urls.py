from django.urls import path
from apps.diario.views import index,login,lista_registros
from django.contrib.auth.views import LogoutView

urlpatterns = [
    ##Pagina base
    path('', index, name='index'),
    ##Login
    path('login/',login, name='login'),
    ##lista_registros
    path('lista_registros/',lista_registros, name='lista_registros'),
    ##logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

