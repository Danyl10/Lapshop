from django.urls import path,include
from products import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.home),
    path('send-email/', views.mail),
    path('add-comment/', views.add_comment),
    path('laptop/', views.laptops),
    path('admin/', admin.site.urls),
]


product_urls = [
    path('laptop-detail/<int:laptop_id>' , views.laptop_detail),
    path('post/', views.posts)
]

urlpatterns += product_urls