
from django.urls import path, include

from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.asview(), name='signup'),
]