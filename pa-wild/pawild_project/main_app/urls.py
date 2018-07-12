from django.conf.urls import url, include
from django.urls import include, path
from main_app import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.AboutView.as_view(),name='main_app/about'),
    url(r'^video/$',views.VideoView.as_view(),name='main_app/video'),
    url(r'^bushcraft/$',views.BushcraftView.as_view(),name='main_app/bushcraft'),
    url(r'^tenkara/$',views.TenkaraView.as_view(),name='main_app/tenkara'),
    url(r'^photo/$',views.PhotoView.as_view(),name='main_app/photo'),
    url(r'^message/$',views.MessageView.as_view(),name='main_app/message'),
    url(r'^users/$',views.users,name='users'),
    # url(r'^messagepage/',views.post,name='post'),

]
