from django.urls import path,include
from . import views

urlpatterns = [
    path('inventory/', views.ItemListView.as_view(), name='inventory'),
    path('', views.HomeView.as_view(), name='home'),
    path('inventory/update_item/<int:pk>/', views.UpdateItemView.as_view(), name='update_item'),
    path('inventory/delete_item/<int:pk>/', views.DeleteItemView.as_view(), name='delete_item'),
    path('inventory/create_item/', views.CreateItemview.as_view(), name='create_item'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('oficina/', views.OficinaView.as_view(), name='oficina'),
    
]
