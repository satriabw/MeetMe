from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from account import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from .utils import AuthRegister, AuthLogin, PostToUserInterest

urlpatterns = [
    url(r'user/$',
        views.UserProfileList.as_view(), name='user-list'),
    url(r'user/(?P<pk>[0-9]+)$',
        views.UserProfileDetails.as_view(), name='user-detail'),
    url(r'^add-interest/$', PostToUserInterest.as_view()),
    url(r'user-interest/$',
        views.UserInterests.as_view(), name='user-interest-list'),
    url(r'user-interest/(?P<pk>[0-9]+)$',
        views.UserInterestDetails.as_view(), name='user-interest-details'),

    url(r'interest/$',
        views.Interests.as_view(), name='interest-list'),
    url(r'interest/(?P<pk>[0-9]+)$',
        views.InterestDetails.as_view(), name='interest-details'),

    url(r'^login/', AuthLogin.as_view()),

    url(r'^register', AuthRegister.as_view(), name='register'),
    url(r'^refresh-token/', refresh_jwt_token),


]