from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about_us"),
    path('catagory_exercise/<cat>/', views.catagory_exercise, name="catagories"),
    path('catagory_chapter/<cat>/<subcatagory>/', views.catagory_chapter, name="catagories_chapters"),
    path('test/<cat>/<subcat>/', views.test, name="test"),
    path('quiz/<cat>/<subcat>/', views.checkquestion, name="quiz"),
]
