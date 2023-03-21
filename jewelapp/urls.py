from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('student/signup/',views.StudentSignUp, name = 'StudentSignup'),
    path('lecturar/signup/',views.LecturerSignUp, name = 'LecturerSignup'),
    path('login/',views.SignInView,name = 'login'),
    path('ghg/',views.tsing,name = 'ghg'),
    path('slog/',views.slog,name = 'slog'),
    path('tlog/',views.tlog,name = 'tlog'),
    path('logout/',views.logout,name = 'logout'),
    path('reactapp/', views.reactapp, name='reactapp'),
]