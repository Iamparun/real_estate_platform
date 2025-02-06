from django.urls import path
from . import views
# from .views import delete_property
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('seller_dashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('buyer_dashboard/', views.buyer_dashboard, name='buyer_dashboard'),
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/<int:property_id>/', views.edit_property, name='edit_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:pk>/details/', views.property_detail_buyer, name='property_detail_buyer'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),

]
