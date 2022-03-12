from django.urls import path
from . import views

app_name="character"
urlpatterns = [
    path('index/<bpk>',views.index,name="index"),
    path('detail/<bpk>',views.detail,name="detail"),
    path('delete/<bpk>/<rpk>',views.delete,name="delete"),
    path('create/<bpk>',views.create,name="create"),
    path('update/<bpk>/<rpk>',views.update,name="update")
]