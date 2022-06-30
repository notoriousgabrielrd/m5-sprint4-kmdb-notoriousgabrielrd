from django.urls import path
from .views import RegisterView

urlpatterns = [
path("users/register/", RegisterView.as_view())

]