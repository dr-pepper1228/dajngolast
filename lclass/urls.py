from django.urls import path
from . import views

app_name="lclass"
urlpatterns = [
    path('index/',views.index,name="index"),
    path('detail/<bpk>',views.detail,name="detail"),
    path('creply/<bpk>',views.creply,name="creply"),
    path('dreply/<bpk>/<rpk>',views.dreply,name="dreply"),
    path('likey/<bpk>',views.likey, name="likey"),
    path('cancel/<bpk>',views.cancel,name="cancel"),
]