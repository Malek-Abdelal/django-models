from django.urls import path
from .views import SnackListView, SnacksDetailsView
urlpatterns = [
    path('', SnackListView.as_view(), name='snacks'),
    path('snacks/<pk>/', SnacksDetailsView.as_view(), name='snacks_details')
]