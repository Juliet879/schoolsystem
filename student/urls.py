from django.urls import path
from .views import register_student,student_list,edit_student,student_profile,delete_student
# from django.contrib.auth.decorators import login_required


urlpatterns = [
    
        path("register/",register_student,name="registerStudent"),
    # path("register/",register_stuent),name="registerStudent"),
    path("student_list/",student_list,name="viewStudents"),
    path("edit/<int:id>/",edit_student,name="editStudent"),
    path("profile/<int:id>/",student_profile,name="profile"),
    path("delete/<int:id>/",delete_student,name="deleteStudent"),
    

]