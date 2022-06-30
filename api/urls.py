from django.urls import path

from api import views


urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('book-list/', views.showAll, name='book-list'),
    path('book-detail/<int:pk>', views.viewBook, name='book-detail'),
    path('book-create/', views.createBook, name='book-create'),
    path('book-update/<int:pk>', views.updateBook, name='book-update'),
    path('book-delete/<int:pk>', views.deleteBook, name='book-delete'),




]
