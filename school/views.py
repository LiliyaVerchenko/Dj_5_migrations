from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students = Student.objects.prefetch_related('teacher').order_by('group')
    context = {'object_list': students}
    return render(request, template, context)
