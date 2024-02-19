from django.shortcuts import render
from .models import Contact, OperationHour, Gallery, Item, Category

# Create your views here.


def index(request):
    contact = Contact.objects.first()
    hours = OperationHour.objects.all()
    pictures = Gallery.objects.all()
    return render(
        request,
        "cms/index.html",
        {"contact": contact, "hours": hours, "pictures": pictures},
    )


def menu(request):
    contact = Contact.objects.first()
    menu = Item.objects.all()
    categories = Category.objects.all()
    hours = OperationHour.objects.all()
    return render(
        request,
        "cms/menu.html",
        {"contact": contact, "menu": menu, "categories": categories, "hours": hours},
    )
