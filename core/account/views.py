from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import Student
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Document
from django.http import HttpResponse

# Create your views here.
@login_required(login_url="/login/")
def documents(request):
    lt=Student.objects.filter(user=request.user.id)
    f_name=lt[0].first_name
    queryset=Document.objects.filter(student_id=lt[0])
    context={"Documents":queryset,
             "firstname":f_name}
    return render(request,'document.html',context)

def home_page(request):
    return render(request,'home.html')

@login_required(login_url="/login/")
@csrf_exempt
def add_document(request):
    if request.method == "POST":
        data=request.POST
        k=request.user
        lt=Student.objects.filter(user=k)
       
        
        document_name=data.get("D_name")
        document_number=data.get("D_no")
        document_type=data.get("D_type")
        document_image=request.FILES["Doc_Image"]
        
        doc1=Document.objects.create(
            Document_no=document_number,
            Document_type=document_type,
            Document_name=document_name,
            Doc=document_image,
            student_id=lt[0]
            
        )
        doc1.save()
    return render(request,'add_document.html')

def login_page(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            messages.info(request,"Invalid User Name")
            return redirect("/login/")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Invalid Password")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect('/add-documents/')
        
    return render(request,"login.html")

def log_out(request):
    logout(request)
    return redirect("/login/")


def register_page(request):
    if request.method =="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        Phone=request.POST.get("mnumber")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request, "User name already taken")
            return redirect("/register/")
        
          
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            # email=email
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")
        student=Student.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            Phone_number=Phone,
            email=email,
            student_id=username
             
        )
        student.save()
        return redirect("/register-page/")
    return render(request,"register.html")

def delete_doc(request,id):
    querset=Document.objects.get(id=id)
    print("hello",querset)
    querset.delete()
    #return HttpResponse(id)
    return redirect("/documents/")

def update_doc(request,id):
    querset=Document.objects.get(id=id)
    
    if request.method=="POST":
        data=request.POST
        
        document_name=data.get("D_name")
        document_number=data.get("D_no")
        document_type=data.get("D_type")
        document_image=request.FILES.get("Doc_Image")
        #print(document_image)
        
        querset.Document_name=document_name
        querset.Document_no=document_number
        querset.Document_type=document_type
        if document_image:
            querset.Doc=document_image
        querset.save()
        return redirect("/documents/")

        
    context={"document":querset}
    return render(request,'update.html',context=context)
    
    