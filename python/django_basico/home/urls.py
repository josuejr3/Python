from django.contrib import admin
from django.urls import path

from home import views as home_views
from blog import views as blog_views

# Request - Response

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", blog_views.my_view),
    path('', home_views.home),
]
