from django.urls import path, include
from .views import *

urlpatterns = [
    # path('user_profile/', Record.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # path('login/', Login.as_view(), name="login"),
    # path('logout/', Logout.as_view(), name="logout"),
]
