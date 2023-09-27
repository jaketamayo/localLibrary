"""
Note that you now have 2 urls.py files in your project – one in the ‘catalog’
directory and one in the ‘locallibrary’ directory. Each app you add to a project will typically have its own
urls.py file, and the main urls.py file in the project-level directory will have an ‘include’ statement to
include the urls in each app.

"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', views.BookDetailView.as_view(), name='book_detail'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('author_detail/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail')
]