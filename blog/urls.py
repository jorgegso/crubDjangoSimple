from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BlogCreateView, BlogDatailView, BlogsListView, BlogUpdateView, BlogDeleteView

app_name="blog"

urlpatterns = [
  path('', BlogsListView.as_view(), name="home"),
  path('create/', BlogCreateView.as_view(), name="create"),
  path('<int:pk>/', BlogDatailView.as_view(), name="detail"),
  path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
  path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")
]
