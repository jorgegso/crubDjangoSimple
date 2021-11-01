from django.db import models

# Create your models here.
#Crear un modelo
#Cada ves que hacemos un cambios en models tenemos que hace una migracion
class Post(models.Model):
  #Cuatos caractares permitodos para rellenar
  title=models.CharField(max_length=250)
  #Campo de texto mas grande para rrellenar contenido
  content=models.TextField()
  
  #self hace referencioa al Post
  #hacer que se vea mas bonito
  #hacer que figure el titulo que le dimos 
  def __str__(self):
      return self.title