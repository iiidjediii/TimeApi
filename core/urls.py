from django.urls import path

from .views import TimeCheckView

urlpatterns = [
    path('', TimeCheckView.as_view()),
]
