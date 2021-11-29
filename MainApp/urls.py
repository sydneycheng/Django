from django.urls import path

from . import views

app_name = "MainApp"

urlpatterns = [
    path("", views.index, name="index"),
    path("topics", views.topics, name="topics"),
    # we've created an integer variable to distinguish via a PK for chess, rock climbing, etc
    # this acts as an identifying value
    path("topics/<int:topic_id>/", views.topic, name="topic"),
]
