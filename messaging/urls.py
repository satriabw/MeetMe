from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from messaging import views

urlpatterns = [
	url(r'post/$',
        views.MessagePosting.as_view(), name='message'),
]