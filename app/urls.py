from django.urls import path
from app import views


urlpatterns = [
    path('', views.homeview, name='home'),
    path('profile/', views.profileview, name='profile_view'),
    path('profile/edit/',views.profile_edit,name='profile_edit'),
    
    path('pets/add',views.add_pets,name='add_pets'),
    path('pets/view',views.view_pets,name='view_pets'),
    path('pets/delete/<int:pk>',views.delete_pets,name='delete_pets'),
    path('pets/edit/<int:pk>',views.edit_pets,name='edit_pets'),
    path('pets/detail/<int:pk>',views.view_pet_by_id,name='view_pet_by_id'),
    path('pets/board',views.board_pet,name='board_pets'),

    path('board/view',views.view_boarding,name='view_boarding'),
    path('board/delete/<int:pk>',views.delete_boarding,name='board_delete'),
    path('payments/view',views.view_payment,name='view_payments'),
    path('payments/make/<int:pk>',views.make_payment,name='make_payment')

]