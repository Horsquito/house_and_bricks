from .views import StatsListView, CreateHouse, HouseDetailView, CreateTask
from django.urls import path


app_name = 'brick_counter'
urlpatterns = [
    path('stats/', StatsListView.as_view(), name='stats'),
    path('building/', CreateHouse.as_view(), name='building'),
    path('building/<int:pk>', HouseDetailView.as_view(), name='house_page'),
    path('building/<int:pk>/add_bricks/', CreateTask.as_view(), name='create_task')
]
