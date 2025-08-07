from django.shortcuts import render

# Create your views here.
import requests
def homepage(request):
    try:
        response=request.get('http://localhost:8000/api/menu')
        menu_items=response.json()
    except requests.exceptions.RequestException:
        menu_items=[]
    return render(request,'menu/homepage.html', {'menu_items':menu_items})