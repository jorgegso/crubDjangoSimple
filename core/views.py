from django.views.generic import View
from django.shortcuts import render


class Homeview(View):
  #cualquier varible que objeto de lo que llammos pueda tener
  def get(self, request, *args, **kwards):
    context={
      
    }
    return render(request, 'index.html', context)









