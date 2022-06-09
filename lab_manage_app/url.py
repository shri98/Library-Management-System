from django.urls import include, path
from lab_manage_app import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add_book/', views.addbook, name='addbook'),
    path('viewbooks/<int:book_id>/', views.viewbook, name='viewbook'),
    path('update_book/<int:book_id>/', views.updatebook, name='updatebook'),
    path('delete_book/<int:book_id>/', views.deletebook, name='deletebook'),

]
