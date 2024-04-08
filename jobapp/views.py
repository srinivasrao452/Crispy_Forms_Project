from django.http import HttpResponse
from django.shortcuts import render,redirect
from jobapp.models import Employee,Position, Post
from jobapp.forms import Employee_ModelForm,Position_ModelForm

def EmployeeCreateView(request):
    if request.method=='POST':
        form = Employee_ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
            # return HttpResponse('Saved')
        else:
            context = {
                "error" : "Employee record not created successfully"
            }
            return render(request,'employee_create.html',context)
    else:
        form = Employee_ModelForm()
        context = {
            "form" : form
        }
        return render(request,'employee_create.html',context)

def EmployeeListView(request):
    employee_list = Employee.objects.all()
    context = {
        "employee_list" : employee_list,
        "error" : "Employees data not available"
    }
    return render(request, 'employee_list.html',context)

def PositionCreateView(request):
    if request.method=='POST':
        form = Position_ModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posistion_list')
        else:
            context = {
                "error": "Posistion record not created successfully"
            }
            return render(request, 'position_create.html', context)
    else:
        form = Position_ModelForm()
        context = {
            "form" : form
        }
        return render(request,'position_create.html',context)

def PositionListView(request):
    posistion_list = Position.objects.all()
    context = {
        "posistion_list" : posistion_list,
        "error" : "Position data not available"
    }
    return render(request, 'position_list.html',context)


from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage

def index(request):
    # fetching all post objects from database
    posts = Post.objects.all()
    # creating a paginator object
    p = Paginator(posts, 2)
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        # returns the desired page object
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {
        "page_obj" : page_obj
    }
    return render(request,'index.html', context)






















