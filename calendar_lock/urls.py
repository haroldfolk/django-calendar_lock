from django.conf.urls import url

from calendar_lock.views import index

urlpatterns = [

    url(r'^$', index,name='index' )
]