
from django.contrib import admin
from jobapp.models import Employee,Position,Post

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','fullname','mobile','emp_code','position']
    search_fields = ['fullname']
    list_filter = ['position']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['id','title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author', 'date_posted','content']


