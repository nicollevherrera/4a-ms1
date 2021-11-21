from django.urls import path
from .views import UserListCreate,UserUpdateDelete, RoleListCreate, RoleUpdateDelete 

urlpatterns = [
    path('rol/' , RoleListCreate.as_view()),
    path('rol/<pk>/', RoleUpdateDelete.as_view()),
    path('usuario/', UserListCreate.as_view()),
    path('usuario/<pk>/', UserUpdateDelete.as_view())
]