from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'pcmapp'
urlpatterns = [
    #display list of members
    path('',views.IndexView.as_view(), name='index'),
    #get by car number
    path('<int:pk>/',views.DetailView.as_view(), name='member'),
    #display list of payees
    path('payment/',views.PaymentInYearView.as_view(),name='payment'),
    path('member/login', auth_views.login, name='login'),
    path('member/registration/',views.NewMemberRegistrationView.as_view(),name='newregistration'),
    path('member/registration/registrationsuccess/',views.RegistrationSuccess.as_view(),name='registrationsuccess'),
    path('member/registration/car', views.NewCarRegistrationCreate.as_view(), name='newcarregistration'),
    path('member/sccheck',views.SCcheckView.as_view(),name='sccheck'),
]