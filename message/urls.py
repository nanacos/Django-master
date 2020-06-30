from django.contrib import admin
from django.urls import path, include
from message.views import MessageView

urlpatterns = [
    path("messages", MessageView.as_view()),
]
