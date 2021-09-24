from django.views import View
from .models import API
from django.http import JsonResponse
from django.forms.models import model_to_dict

class APIpListViews(View):
    def get(self, request):
        alist = API.objects.all()
        return JsonResponse(list(alist.values()), safe=False)
              
class APIpDetailViews(View):
    def get(self, request, pk):
        dlist = API.objects.filter(pk=pk)
        return JsonResponse(model_to_dict(dlist))