from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, Meal, School
from .forms import PatientForm, MealForm, SchoolInfo, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def clinic_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            return redirect('clinic_form')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #if ( username == "clinic" or username == "admin"):
            return redirect('dashbord')
            #else:
                #return redirect('home')
        else:
            messages.info(request, 'Username Or Password is incorrect')
            return render(request, 'clinicform.html')
            
    else:
        return render(request, 'clinicform.html',{})
    
def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('clinic_form')
    return render(request, 'register_user.html',{'form':form})
    
def dashbord(request):
    return render(request, 'dashbord.html',{})

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')

def patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('history')
    return render(request, 'patientsform.html',{})

def history(request):
    all_members = Student.objects.all
    return render(request, 'table.html',{'all': all_members})

def special_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('dashbord')
    return render(request, 'specialmeal.html',{})

def school_regard(request):
    if request.method == 'POST':
        form = SchoolInfo(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('dashbord')
    return render(request, 'schoolregard.html',{})

def school_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            return redirect('school_form')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #if ( username == "school" or username == "admin"):
            return redirect("school")
            #else:
                #return redirect("home")
        else:
            # Return an 'invalid login' error message.
            messages.info(request, 'Username Or Password is incorrect')
            return redirect("school_form")
    else:
        return render(request, 'schoolform.html',{})
    
def school_register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('school_form')
    return render(request, 'school_register_user.html',{'form':form})
    
def school(request):
    all_members = School.objects.all
    return render(request,'theschool.html',{'all': all_members})

def kitchen_form(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            return redirect("kitchen_form")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #if username == "kitchen" or username == "admin":
            return redirect("kitchen")
            #else:
                #return redirect("home")
        else:
            messages.info(request,'Username Or Password is incorrect')
            return redirect("kitchen_form")  
    else:
        return render(request, 'kitchenform.html',{})
    
def kitchen_register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            return redirect('kitchen_form')
    return render(request, 'kitchen_register_user.html',{'form':form})
    
def kitchen(request):
    all_members = Meal.objects.all
    return render(request, 'kitchenhomepage.html',{'all': all_members})