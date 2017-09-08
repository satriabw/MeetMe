from django.conf.urls import url
from matchmaking import views
from .utils import *


urlpatterns = [
    url(r'interest-matrix/$',
        views.InterestMatrixList.as_view(), name='interest-matrix-list'),
    url(r'matchmaking-engine/$',
        MatchmakingEngine.as_view(), name='matchmaking-engine'),
]