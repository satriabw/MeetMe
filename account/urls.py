from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views
from rest_framework_jwt.views import obtain_jwt_token
from .utils import AuthRegister

urlpatterns = [
    url(r'user/$',
        views.UserProfileList.as_view(), name='user-list'),
    url(r'user/(?P<pk>[0-9]+)$',
        views.UserProfileDetails.as_view(), name='user-detail'),
    url(r'interests/$',
        views.Interests.as_view(), name='interest-list'),
    url(r'interest/(?P<pk>[0-9]+)$',
        views.InterestDetails.as_view(), name='interest-details'),
    url(r'^login/', obtain_jwt_token),
    url(r'^register', AuthRegister.as_view(), name='register'),

]