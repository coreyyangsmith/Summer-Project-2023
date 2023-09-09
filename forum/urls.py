from django.urls import path, re_path

from . import views

urlpatterns = [

    path("", views.NeighbourhoodListView.as_view(), name="neigbourhoods"), # /forum/
    re_path(r'^[A-Z]{3}/$', views.CategoryListView.as_view(), name="categories"), # /forum/COU/ 
    re_path(r'^[A-Z]{3}/\d+/$', views.ThreadListView.as_view(), name="threads"), # /forum/COU/1234/
    re_path(r'^[A-Z]{3}/\d+/\d+', views.PostListView.as_view(), name="posts"), # /forum/COU/1234/123
    
    path('<pk>/detail/', views.NeigbourhoodDetailView.as_view(),  name='neighbourhood-detail'), #/forum/1/
    
    re_path(r'^api/categories/$', views.categories_list),
    #re_path(r'^api/categories/([0-9])$', views.sessions_detail),  

    re_path(r'^api/threads/$', views.threads_list),
    #re_path(r'^api/categories/([0-9])$', views.sessions_detail),  

    re_path(r'^api/posts/$', views.posts_list),
    #re_path(r'^api/categories/([0-9])$', views.sessions_detail),   
 ]

