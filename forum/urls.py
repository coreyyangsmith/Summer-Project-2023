from django.urls import path, re_path

from . import views

urlpatterns = [

    path("", views.NeighbourhoodListView.as_view(), name="neigbourhoods"), # /forum/
    re_path('^[A-Z]{3}/$', views.CategoryListView.as_view(), name="categories"), # /forum/COU/
    re_path('^[A-Z]{3}/\d+/$', views.ThreadListView.as_view(), name="threads"), # /forum/COU/1234/
    re_path('^[A-Z]{3}/\d+/\d+', views.PostListView.as_view(), name="posts"), # /forum/COU/1234/123
]