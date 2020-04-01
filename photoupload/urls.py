from django.urls import path
from . import views

urlpatterns = [
    path('', views.explore, name='photoupload'),
    path('photoupload', views.FileFieldView.as_view(), name='FileFieldView'),
    path('login', views.login, name='login'),
    path('inspect/<key>', views.inspect, name='inspect')
    # path('success', views.FileFieldView.as_view(), name='FileFieldView')
]
