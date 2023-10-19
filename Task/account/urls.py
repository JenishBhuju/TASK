from django.urls import path
from account.views import  UserLoginView, UserProfileView, UserRegistrationView, StudentRegistrationView, StudentLoginView, TeacherRegistrationView, TeacherLoginView
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    
    path('student/register/', StudentRegistrationView.as_view(), name='student-register'),
    path('student/login/', StudentLoginView.as_view(), name='student-login'),
   
    # Teacher URLs
    path('teacher/register/', TeacherRegistrationView.as_view(), name='teacher-register'),
    path('teacher/login/', TeacherLoginView.as_view(), name='teacher-login'),
 
]