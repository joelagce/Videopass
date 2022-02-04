from django.urls import path

from  . import views

urlpatterns = [
	#Leave as empty string for base url

    path('', views.home, name="home"),
	path('cart/', views.cart, name="cart"),
	path('store/', views.store, name="store"),
	path('checkout/', views.checkout, name="checkout")

]