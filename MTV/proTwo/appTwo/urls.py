from django.conf.urls import url
from appTwo import views

urlpatterns = [
    url('',views.users,name = 'users')
]
