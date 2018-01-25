from django.conf.urls import url
from .views import homepage, showpost

urlpatterns = [
    url(r'^$', homepage),
    url(r'^post/(\w+)$', showpost),
]