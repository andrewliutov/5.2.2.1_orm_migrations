from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    students_query = Student.objects.all().prefetch_related('teachers').order_by(ordering)
    context = {'object_list': students_query}

    return render(request, template, context)
