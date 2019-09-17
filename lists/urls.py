from django.urls import path
from lists.views import view_list, new_list, add_item

urlpatterns = [
    path('<int:list_id>/', view_list),
    path('<int:list_id>/add_item', add_item),
    path('new', new_list),
]
