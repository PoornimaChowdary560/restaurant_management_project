from django.shortcuts import render
def menu_list(request):
    menu_items=[
        {"name":"pizza", "price":8.99, "description":"classic cheese pizza with tomato sauce"},
        {"name":" Veggie burger", "price":6.99, "description":"grilled veggie patty with lettuce and tomato" }
        {"name":"pasta Alfredo", "price":7.99, "description":"creamy alfredo sauce over fettuccine pasta"}
    ]
    return render(request, 'menu_list.html', {'menu_items':menu_items})