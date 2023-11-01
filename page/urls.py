
from django.urls import path
from .views import login_view,reg_view,home_view,finance_view

urlpatterns = [
    # Other URL patterns
    path('login/', login_view, name='login'),
    path('registration', reg_view,name='registration'),
    path('home', home_view,name='home'),
    path('finance', finance_view,name='finance'),

]
