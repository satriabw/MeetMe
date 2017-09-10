from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^message/$',
        views.ListMessageView.as_view(), name='message-list'),
    url(r'^send/$', views.MessageEngine.as_view(), name="send-message"),
]