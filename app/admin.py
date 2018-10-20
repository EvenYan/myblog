from django.contrib import admin

# Register your models here.
from app.models import Grade, Student


class StudentTable(admin.StackedInline):
    model = Student
    extra = 5


class GradeModelAdmin(admin.ModelAdmin):
    inlines = [StudentTable]



def gender(self):
    if self.s_sex:
        return "男"
    return "女"
gender.short_description = "性别"


class StudentModelAdmin(admin.ModelAdmin):
    list_display = ("s_name", gender, "s_grade")


admin.site.register(Student, StudentModelAdmin)
admin.site.register(Grade, GradeModelAdmin)