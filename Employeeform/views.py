from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
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
    paginator = Paginator(students,25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'allemployees.html',{"page_obj":page_obj})
def employee(request,employeeid):
    employee = Employee.objects.get(pk=employeeid)
    return render(request,'employee.html',{"employee":employee})
def delete_employee(request,employeeid):
    employee_del = get_object_or_404(Employee,pk=employeeid)
    employee_del.delete()
    return redirect('allemployees')
def search_employee(request):
    search = request.GET.get('search')
    rendered_data = Employee.objects.filter(Q(name__icontains=search))
    return render(request,'allemployees.html',{"page_obj":rendered_data})