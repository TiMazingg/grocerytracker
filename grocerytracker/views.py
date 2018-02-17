from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ProductForm
from .models import Product

# Create your views here.

def index(request):
    return HttpResponse('Test')

def display_products(request):
    template_variables = {}
    products = Product.objects.all().order_by('product')
    template_variables['products'] = products

    for product in products:
        print(product)

    return render(request, 'grocerytracker/display_products.html', template_variables)

def submit_product(request):
    # If POST, process form data
    if request.method == 'POST':
        # Create a form and populate
        form = ProductForm(request.POST)

        # Check if valid, and handle
        if form.is_valid():
            # check if product already exists
            product_list = Product.objects.filter(product=form.cleaned_data['product']).order_by('store')
            if product_list.count() > 0:  # already exists
                # Check price
                print('here1')
                print(product_list.first().price)
                print('here2')
                if form.cleaned_data['price'] < product_list.first().price:
                    print('here3')
                    product_list.first().delete()
                    Product.objects.create(
                        product=form.cleaned_data['product'],
                        price=form.cleaned_data['price'],
                        store=form.cleaned_data['store']
                    )
            else:
                Product.objects.create(
                    product=form.cleaned_data['product'],
                    price=form.cleaned_data['price'],
                    store=form.cleaned_data['store']
                )
            return HttpResponseRedirect('displayproducts')
    # Else, create blank form
    else:
        form = ProductForm()

    return render(request, 'grocerytracker/submit_product.html', {'form': form})