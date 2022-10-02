from django.urls import path
from . import views
from knox import views as knox_views


urlpatterns = [
    path('teachers/',views.teacherApi, name='teachers' ),
    path('login/', views.LoginAPI.as_view(), name='login'),
    path('registerteacher/', views.RegisterAPI.as_view(), name='register'),
    path('Quicklab/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('Quicklab/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    # path('teacher-detail/<int:id>', views.TeacherDetailAPIView.as_view()),
    # path('teacher/<int:id>', views.GenericAPIView.as_view()),
    # path('teacher', views.GenericAPIView.as_view()),
    
]