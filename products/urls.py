from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('products/', views.ListProductsAPI.as_view(), name = 'products'),
    path('products/<int:pk>/', views.DetailProductApi.as_view(), name = 'product-detail'),
    path('orders/', views.OrderListCreateAPI.as_view(), name = 'orders'),
    path('orders/<int:pk>/', views.OrderUpdateReytrieveDestroy.as_view(), name = 'order-detail'),
    path('cart/', views.CartListCreate.as_view(), name = 'cart'),
    path('cart/<int:pk>', views.CartDetail.as_view(), name = 'cart-detail'),
    path('states/buyer/', views.OrderStateBuyerList.as_view(), name='states_buyer'),
    path('states/owner/', views.OrderStateOwnerList.as_view(), name = 'states_owner'),
    path('states/<int:pk>/', views.OrderStateDetail.as_view(), name='orderstate-detail'),
    path('',views.api_root, name = 'root'),
    path('account/register', views.UserCreate.as_view(), name = 'register'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),





]