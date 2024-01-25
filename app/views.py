from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def jadval(request):
    # return HttpResponse("Restoranimizda szni korib turganmzdan hursandmiz")
    return render(request=request, template_name="jadval.html", context={})

def menyu(request):
    return HttpResponse("Menyuga hush kelibsiz")