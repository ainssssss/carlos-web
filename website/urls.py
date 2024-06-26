from django.urls import path
from . import views

app_name = 'website'
urlpatterns=[
    path('',views.index_view, name='index'),   
    path('login/', views.login_view, name='login'),
    path('addbook/', views.addbook_view, name='addbook'),
    path('register/', views.register_view, name='register'),
    path('<int:book_id>/book/', views.book_id_view, name='book_change_value'),
]
