from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.sesrch),
    url(r'^post/(\d+)$', views.showinfo),
]