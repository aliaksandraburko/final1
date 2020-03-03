

from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    #####################home_page###########################################
    path('',views.index,name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<int:item_id>',views.remove,name="del"),
    path('admin/', admin.site.urls),
    path('check/<int:item_id>',views.check,name="check"),
    path('complete/<int:todo_id>', views.completeTodo, name='complete'),
    path('edit/', views.edit, name='edit'),


]