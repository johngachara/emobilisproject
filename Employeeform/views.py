from django.shortcuts import render, redirect
from .forms import Employeeform
from .models import Employee
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = Employeeform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = Employeeform()
    form = Employeeform()
    return render(request,'home.html',{"form":form})
def all_employees(request):
    students = Employee.objects.all()
    return render(request,'allemployees.html',{"students":students})
def employee(request,employeeid):
    employee = Employee.objects.get(pk=employeeid)
    return render(request,'employee.html',{"employee":employee})