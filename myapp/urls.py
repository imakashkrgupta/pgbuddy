from django.contrib import admin
from django.urls import path
from myapp import views as myapp_views
from django.conf.urls import handler404

urlpatterns = [
    path('', myapp_views.index),
    path('home', myapp_views.index),
    path('search', myapp_views.search),
    path('search-data', myapp_views.searchdata, name='search-data'),
    # path('result', myapp_views.result),
    path('result/<int:post_id>', myapp_views.result),
    path('signup', myapp_views.signup),
    path('login', myapp_views.login),
    path('dashboard', myapp_views.dashboard),
    path('add-post', myapp_views.add_post),
    path('all-post', myapp_views.all_post),
    path('delete-post/<str:post_id>', myapp_views.delete_post),
    path('deactivate-post/<int:post_id>', myapp_views.deactivate_post),
    path('activate-post/<int:post_id>', myapp_views.activate_post),
    path('edit-post/<str:post_id>', myapp_views.edit_post),
    path('logout', myapp_views.logout),
    # path('delall', myapp_views.delall),
]

