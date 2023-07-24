from django.shortcuts import render, redirect, HttpResponse
from .models import Department, Employee, Role
from datetime import datetime 
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = int(request.POST.get('salary'))
        bonus = int(request.POST.get('bonus'))
        phone = int(request.POST.get('phone'))
        dep = int(request.POST.get('dep'))
        role = str(request.POST.get('role'))
        new_emp = Employee(first_name = first_name,
                           last_name = last_name,
                           salary = salary,
                           bonus = bonus,
                           phone = phone,
                           dep_id = dep,
                           role_id = role,
                           hire_data = datetime.now())
        new_emp.save()
        return redirect("/")
    elif request.method=="GET": 
        return render(request, 'add_emp.html')
    else:
        return HttpResponse("An Exception Occured! Employee Has Not Been Added")

def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete() 
            return redirect('/')    
        except:
            return HttpResponse("Please Enter Avalid EMP ID")
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'remove_emp.html', context )

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dep = request.POST.get('dep')
        role = request.POST.get('role ')
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dep:
            emps = emps.filter(dep__name__icontains = dep)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context = {
            'emps' : emps
        }
        print("haresh")
        return render(request, 'view_all_emp.html', context)
    elif request.method == 'GET':
        print("haresh")
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('An Exception Occurred')