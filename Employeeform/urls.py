from django.conf.urls.static import static
from django.urls import path

from Emobilisproject3 import settings
from .  import views
urlpatterns = [
    path('',views.home,name='home'),
    path('all/',views.all_employees,name='allemployees'),
    path('employee/<int:employeeid>',views.employee,name='employee'),
    path('employee/delete/<int:employeeid>',views.delete_employee,name='delete'),
    path('search/',views.search_employee,name='search'),
    path('employee/update/<int:employeeid>',views.update_employee,name='update')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)