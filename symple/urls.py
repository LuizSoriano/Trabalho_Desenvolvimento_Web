from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import auth_views as custom_auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/<int:evento_id>/', views.detalhe_evento, name='detalhe_evento'),
    path('comprar/<int:ingresso_id>/', views.comprar_ingresso, name='comprar_ingresso'),
    path('checkout/<int:compra_id>/', views.checkout, name='checkout'),
    path('confirmacao/<int:pagamento_id>/', views.confirmacao_compra, name='confirmacao_compra'),
    path('minhas-compras/', views.minhas_compras, name='minhas_compras'),
    path('perfil/', views.perfil_cliente, name='perfil_cliente'),
    path('register/', custom_auth_views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),
    path('logout-confirm/', views.logout_confirm, name='logout_confirm'),
    path('accounts/logout/', views.custom_logout, name='account_logout'),
]
