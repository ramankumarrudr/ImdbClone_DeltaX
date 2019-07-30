from django.contrib import admin
from django.urls import path,re_path
from django.urls import include
from django.conf.urls import url
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'), 
    re_path(r'^tvshow/$', views.tvshows,name='tvshow'),
    re_path(r'^actor/$', views.actor_images,name='actor'), 
    re_path(r'^exit/$', views.formexit,name='exit'),  
    re_path(r'^form/$',views.post,name='form'),
    re_path(r'^showform/$',views.post_tvshow,name='show_form'),
    re_path(r'^actor-form/$',views.actor,name='actor_form'),
    re_path(r'^form/(?P<id>\d+)/edit/$',views.movie_update,name="update"),
    re_path(r'^index/(?P<id>\d+)/delete/$',views.movie_delete,name="delete"),
    re_path(r'^showform/(?P<id>\d+)/edit/$',views.tvshow_update,name="update_tvshow"),
    re_path(r'^tvshow/(?P<id>\d+)/delete/$',views.tvshow_delete,name="delete_tvshow"),    
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


