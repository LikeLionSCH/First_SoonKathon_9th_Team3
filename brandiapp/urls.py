from django.urls import path
from brandiapp import views

urlpatterns = [
    # Product
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('product/', views.make_product, name='product'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('mypage', views.mypage, name='mypage'),
    # Review
    path('review/', views.review, name='review'),
    path('review/create/', views.review_create, name='review_create'),
]
