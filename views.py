from django.shortcuts import render 
from.import views

def create(request):
    if request.POST:
        print(request.POST('title'))
    return render(request,'create.html')

def edit(request):
    return render(request,'edit.html')

def list(request):
     
 
     movie_data = { 'movies' : [
        {
            'title' : 'apple',
            'year' : 2001,
            'img' : 'logos.png',
            'success' : False
            
        },
        {  
            'title' : 'orrange',
            'year' : 2005,
            'img' : 'as.jpeg'

        }
    ] 
    }
     return render(request,'list.html',movie_data)
  