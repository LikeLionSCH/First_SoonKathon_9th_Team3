from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def home (request) :
    products = Product.objects.all()
    return render (request, 'home.html', {'products': products})

def mypage (request) :
    return render (request, 'mypage.html')
    
''' Product '''
def detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'detail.html', {'product': product})

def make_product(request):
    if request.method == 'POST':
        new_product = Product()
        new_product.thumbnail = request.FILES.get('thumbnail')
        new_product.detail_image = request.FILES.get('detail_image')
        new_product.product_name = request.POST['product_name']
        new_product.explanation = request.POST['explanation']
        new_product.price = request.POST['price']
        new_product.OPTION = request.POST['OPTION']
        new_product.save()
        return redirect('home')
    else:   # GET 메소드일 때
        return render(request, 'new.html')


def update(request, id):
    if request.method == 'POST':
        update_product = Product.objects.get(pk=id)
        update_product.thumbnail = request.FILES.get('thumbnail')
        update_product.detail_image = request.FILES.get('detail_image')
        update_product.product_name = request.POST['product_name']
        update_product.explanation = request.POST['explanation']
        update_product.price = request.POST['price']
        update_product.OPTION = request.POST['OPTION']
        update_product.save()
        return redirect('detail', update_product.id)
    else:
        product = Product.objects.get(id=id)
        return render(request, 'edit.html', {'product': product})

def delete(request, id):
    delete_product = Product.objects.get(pk=id)
    delete_product.delete()
    return redirect('home')


''' Review '''
def review (request) :
    reviews = Review.objects.all()
    return render(request, 'review.html', {'reviews':reviews})

def review_create(request) :
    review_create = Review()
    review_create.author = request.POST['author']
    review_create.content = request.POST['content']
    review_create.review_image = request.FILE.get('review_image')
    review_create.created_at = timezone.now()
    review_create.save()
    return redirect('review')
