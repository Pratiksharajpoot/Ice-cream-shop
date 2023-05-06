from django.shortcuts import render ,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"My father is the best Father of the world",
        "variable2":"My Mother is really very hard working"
    }
    return render(request,'index.html',context)


def about(request):
     return render(request,'about.html')


def service(request):
    # return HttpResponse("This is service")
     return render(request,'service.html')



def contact(request):
    # return HttpResponse("This is contact")
    if request.method=="POST":
        name=request.POST.get('name'),
        email=request.POST.get('email'),
        phone=request.POST.get('phone'),
        desc=request.POST.get('desc'),
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent!")
        
    return render(request,'contact.html')


