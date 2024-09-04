from django.shortcuts import render, get_object_or_404

from catalog.models import Product


# def home(request):
#     return render(request, 'catalog/home.html')
def base(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')


def product_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, pk):
    context = {
        'product': Product.objects.get(pk=pk)
    }

    return render(request, 'catalog/product_detail.html', context)




