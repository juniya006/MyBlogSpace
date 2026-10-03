from django.urls import path
from django.urls import path, include
from .import views

urlpatterns = [
   path('',views.home,name='home'),
   path('home/',views.home,name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login_view,name='login'),
   path('add-blog/',views.add_blog,name='add_blog'),
   path('blog/<int:id>/',views.blog_detail,name='blog_detail'),
   path('logout/', views.logout_user, name='logout'),
   
]