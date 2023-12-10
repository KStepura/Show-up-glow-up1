from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker_home, name='tracker_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.TrackerDetailView.as_view(), name='tracker-detail'),
    path('<int:pk>/update', views.TrackerUpdateView.as_view(), name='tracker-update'),
    path('<int:pk>/delete', views.TrackerDeleteView.as_view(), name='tracker-delete')
]