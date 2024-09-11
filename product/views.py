from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    categories= Category.objects.all()
    # Paginate categories with 4 categories per page
    paginator = Paginator(categories, 3)
    page_number = request.GET.get('page')  # Get the page number from the query parameter 'page'
    page_obj = paginator.get_page(page_number)
    catwise={}
    for category in page_obj:
        product=Product.objects.filter(category=category).order_by('-price')
        catwise[category]= product
    return render(request,'home.html',{'catwise':catwise,'page_obj':page_obj})


def product(request, pk):
    product=Product.objects.get(id=pk)
    related_products=Product.objects.filter(category=product.category).exclude(id=product.id).order_by('?')[:4]
    return render(request,'product.html',{'product':product,'related_products':related_products})


def category(request, cname):
    try:
        category = Category.objects.get(name=cname)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products,'category':category})
    except:
        return render(request, '404notfound.html', {'cname': cname})


def add_product(request):
    product=""
    if request.method == 'POST' or request.method== "FILES":
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        category_id = request.POST['category']
        image = request.FILES['image']

        # Fetch the Category instance
        category = Category.objects.get(id=category_id)
        
        product = Product.objects.create(name=name, price=price, description=description, category=category, image=image)
        product.save()
        messages.success(request, 'Product Added Successfully')
        return redirect('home')
    
    return render(request,'add_product.html',{'product':product})


def search(request):
    query = request.GET.get('query', '')
    if query:
        products = Product.objects.filter(name__icontains=query)    #The icontains lookup is used to get records that contains a specified value.
    else:
        products = Product.objects.none()
    return render(request, 'search_results.html', {'products': products, 'query': query})


def sale(request):
    products=Product.objects.filter(is_sale=True).order_by('sale_price')
    return render(request,'sale.html',{'products':products})