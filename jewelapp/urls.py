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
    path('dail/', views.dail, name='dail'),
    path('dailret/', views.dret, name='dailret'),
    path('upd/<id>/',views.upda),
    path('del/<id>/',views.delete_view),
    path('slogm/',views.slogm, name='slogm'),
    path('sel/',views.seldail,name='sel'),
    path('up/<id>/',views.up),
    path('de/<id>/',views.de),

]