from django.urls import path
from .views import UserListCreate,UserUpdateDelete, RoleListCreate, RoleUpdateDelete 

urlpatterns = [
    path('role/' , RoleListCreate.as_view()),
    path('role/<pk>/', RoleUpdateDelete.as_view()),
    path('user/', UserListCreate.as_view()),
    path('user/<pk>/', UserUpdateDelete.as_view())
]