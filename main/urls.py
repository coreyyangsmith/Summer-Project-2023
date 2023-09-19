from django.urls import path, re_path

from main import views

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="home"),    
    path("frontend/", views.frontend_test, name="frontend"),
    path("<int:id>", views.index, name="index"),
    re_path(r"vote/(?P<comm_code>[A-Z]{3})", views.vote, name="vote"), #/vote/COU

    re_path(r'^api/communities/$', views.communities_list), # /api/communities/
    #re_path(r'^api/communities/([0-9])$', views.communities_detail),  #   

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)