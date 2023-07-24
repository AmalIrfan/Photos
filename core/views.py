from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_htmx.http import retarget

# Create your views here.
def index(request, page=''):
    if not page:
        return HttpResponseRedirect('home')
    if request.htmx:
        response = render(request, f"{page}.html")
        return retarget(response, "#page-content")
    return render(request, "index.html", {"content": f"{page}.html"})

