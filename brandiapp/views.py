from django.shortcuts import render

# Create your views here.
def home (request) :
    return render (request, 'home.html')

def review (request) :
    reviews = Review.objects.all()
    return render (request, 'review.html', {'reviews':reviews})