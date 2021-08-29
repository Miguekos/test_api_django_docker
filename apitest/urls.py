from django.urls import path, include
from .views import (
    WorkerListApiView,
    WorkerDetailApiView
)

urlpatterns = [
    path('worker', WorkerListApiView.as_view()),
    path('worker/<int:worker_id>', WorkerDetailApiView.as_view()),
]
