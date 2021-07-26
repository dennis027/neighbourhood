from django.conf.urls import url
from django.db.models.query_utils import PathInfo
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns=[
    url(r'^$',views.index, name='index'),
    url('register/',views.register, name='registration'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url(r'profile/', views.profile, name='profile'),
    url(r'emergency/', views.emergency, name='emergency'),
    url(r'neighbor/', views.neighbor, name='neighbor'),
    url(r'^post/', views.post, name="post"),
    url(r'^search/', views.search, name='search'),
    url(r'^logout/$', views.logout_view, name='index'), 
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)