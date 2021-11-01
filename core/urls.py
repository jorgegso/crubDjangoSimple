from django.contrib import admin
from django.urls import path, include

#importamos homeview de core es una view
from .views import Homeview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homeview.as_view(), name="home"),
    #namespace por que llamaremos de otro lado...como desde el template
    path('blog/', include('blog.urls', namespace='blog'))
]
