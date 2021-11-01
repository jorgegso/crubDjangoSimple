from django.urls import path
from django.urls.resolvers import URLPattern
#impotamos de views create y lista de view
from .views import BlogCreateView, BlogDatailView, BlogsListView, BlogUpdateView, BlogDeleteView

app_name="blog"

urlpatterns = [
  #como es una clase ocupamos as_view
  path('', BlogsListView.as_view(), name="home"),
  #aca se accede a create view
  path('create/', BlogCreateView.as_view(), name="create"),
  # int:pk tenemos que pasarle una url
  path('<int:pk>/', BlogDatailView.as_view(), name="detail"),
  #int:pk para update 
  path('<int:pk>/update/', BlogUpdateView.as_view(), name="update"),
  path('<int:pk>/delete/', BlogDeleteView.as_view(), name="delete")
]
