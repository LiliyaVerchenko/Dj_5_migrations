from django.contrib import admin

from school.models import Student, Teacher


class MembershipInline(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        MembershipInline,
    ]

