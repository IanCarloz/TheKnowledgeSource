#Urls de app landing
from django.conf.urls import url
from .views import index
app_name = 'landing'
urlpatterns = [
    url(r'^$',index, name="index"),
]
