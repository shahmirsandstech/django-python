from django.urls import path
from views.person import PersonView
from views.user import UserRegistrationView

urlpatterns = [
    path('person/',PersonView.as_view()),
    path('user/',UserRegistrationView.as_view())
]