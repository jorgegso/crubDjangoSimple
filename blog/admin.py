from django.contrib import admin

# importammos es modelo que hemo creado
from .models import Post

#registrarlo el modelo que hemos creado
admin.site.register(Post)
