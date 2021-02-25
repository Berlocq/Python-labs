"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#from book.views import author_list
from book import views

urlpatterns = [
    path('s-admin/', admin.site.urls),
    path('author/', views.AuthorList.as_view(), name="author-list"),
    path('author/<int:pk>/', views.author_detail, name="author-detail"),
    path('author-cbv/<int:pk>/', views.AuthorDetail.as_view(), name="author-detail-cbv"),
    path('author-delete/<int:pk>/', views.author_delete, name="author-delete"),
    path('author-delete-cbv/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete-cbv"),
    path('author-create/', views.author_create, name="author-create"),
    path('author-create-cbv/', views.AuthorCreate.as_view(), name="author-create-cbv"),
    path('author-update/<int:pk>/', views.author_update, name="author-update"),
    path('author-update-cbv/<int:pk>/', views.AuthorUpdate.as_view(), name="author-update-cbv"),
    path('genre/', views.GenreList.as_view(), name="genre-list"),
    path('genre-cbv/<int:pk>/', views.GenreDetail.as_view(), name="genre-detail-cbv"),
    path('genre-delete-cbv/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete-cbv"),
    path('genre-create-cbv/', views.GenreCreate.as_view(), name="genre-create-cbv"),
    path('genre-update-cbv/<int:pk>/', views.GenreUpdate.as_view(), name="genre-update-cbv"),
    path('series/', views.SeriesList.as_view(), name="series-list"),
    path('series-cbv/<int:pk>/', views.SeriesDetail.as_view(), name="series-detail-cbv"),
    path('series-delete-cbv/<int:pk>/', views.SeriesDelete.as_view(), name="series-delete-cbv"),
    path('series-create-cbv/', views.SeriesCreate.as_view(), name="series-create-cbv"),
    path('series-update-cbv/<int:pk>/', views.SeriesUpdate.as_view(), name="series-update-cbv"),
    path('izdatel/', views.IzdatelList.as_view(), name="izdatel-list"),
    path('izdatel-cbv/<int:pk>/', views.IzdatelDetail.as_view(), name="izdatel-detail-cbv"),
    path('izdatel-delete-cbv/<int:pk>/', views.IzdatelDelete.as_view(), name="izdatel-delete-cbv"),
    path('izdatel-create-cbv/', views.IzdatelCreate.as_view(), name="izdatel-create-cbv"),
    path('izdatel-update-cbv/<int:pk>/', views.IzdatelUpdate.as_view(), name="izdatel-update-cbv"),
]
 