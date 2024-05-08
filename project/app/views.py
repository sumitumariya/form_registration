from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')


def register (request):

    print(request.method)
    print(request.POST)
    # .....................................
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    contact=request.POST.get('contact')
    # print(name)
    # print(email)
    # print(password)
    # print(contact)




    # ......................................................................................
    data= Student.objects.filter(Email=email)
    print(data)
    if data :
        msg="Email already exits"
        return render (request,'home.html',{'key':msg})
    else:
         Student.objects.create(Name=name,Email=email,Contact=contact)
         msg="Registration Successfully"
         return render (request,'login.html',{'key':msg})
    
#    ....................................
#   print(request.POST['name'])
#   print(request.POST['email'])
#   print(request.POST['password'])
#   print(request.POST['contact'])

  


 
