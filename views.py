from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem, RestaurantLocation
def menu_list(request):
    menu_items=[
        {"name":"pizza", "price":8.99, "description":"classic cheese pizza with tomato sauce"},
        {"name":" Veggie burger", "price":6.99, "description":"grilled veggie patty with lettuce and tomato" }
        {"name":"pasta Alfredo", "price":7.99, "description":"creamy alfredo sauce over fettuccine pasta"}
    ]
    return render(request, 'menu_list.html', {'menu_items':menu_items})

def menu_view(request):
    try:
        items=MenuItem.objects.all()
        return render(request, 'menu.html', {'items':items})
    except Exception as e:
        return HttpResponse(f"As error occured while loading the menu {str(e)}", status=500)

def homepage(request):
    location=RestaurantLocation.objects.first()
    return render(request, 'homepage.html', {'location':location})