from django.urls import path
from django.contrib import admin
from crm import views
from permitter import views as permitter_views
from owner import views as owner_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('add-customer/', views.add_customer, name='add_customer'),
    path('base', views.base, name='base'),
    path('add-message/', views.add_message, name='add_message'),
    path('add-churn/', views.add_churn_feature, name='add_churn'),
    path('add-purchase/', views.add_purchase, name='add_purchase'),
    path('success/', views.success, name='success'),
    path('view-customers/', views.view_customers, name='view_customers'),
    path('view-messages/', views.view_messages, name='view_messages'),
    path('view-purchases/', views.view_purchases, name='view_purchases'),
    path('view-churn/', views.view_churn_features, name='view_churn'),
    path('predict_sentiment/', views.predict_sentiment, name='predict_sentiment'),
    path('dataset/', views.dataset_view, name='dataset'),
    path('customer_dashboard/', views.customer_dashboard, name='customer_dashboard'),



    path('', permitter_views.main, name='main'),
    path('index/', permitter_views.index, name='index'),
    path('permitter_base/', permitter_views.permitter_base, name='permitter_base'),
    path('admin_login/', permitter_views.admin_login, name='admin_login'),
    path('owner_login/', permitter_views.owner_login, name='owner_login'),

    path('register/', owner_views.register_user, name='register'),
    path('view_users/', owner_views.view_users, name='view_users'),
    path('delete_user/<int:user_id>/', owner_views.delete_user, name='delete_user'),
    path('activate_user/<int:user_id>/', owner_views.activate_user, name='activate_user'),
    path('deactivate_user/<int:user_id>/', owner_views.deactivate_user, name='deactivate_user'),
    path('userlogin/', owner_views.user_login, name='userlogin'),
]
