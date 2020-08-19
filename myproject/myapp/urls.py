from django.urls import path
from .views import view1 as v1
from .views import view2 as v2
from .views import view3 as v3
from django.conf.urls import url, include

urlpatterns = [

    path('hello/', v1.hello),
    path('branch/', v2.branch),
    path('year/', v3.year)
]
