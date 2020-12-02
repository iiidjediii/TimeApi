from django.urls import path

from .views import TimeCheckView

urlpatterns = [
    path('time', TimeCheckView.as_view()),
]
