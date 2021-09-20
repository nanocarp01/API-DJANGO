from django.views import View
from .models import APIad
from django.http import JsonResponse
from django.forms.models import model_to_dict

class APIpListViews(View):
    def get(self, request):
        alist = APIad.objects.all()
        return JsonResponse(list(alist.values()), safe=False)
              
class APIpDetailViews(View):
    def get(self, request, pk):
        dlist = APIad.objects.filter(pk=pk)
        return JsonResponse(model_to_dict(dlist))