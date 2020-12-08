from django.shortcuts import render
from django.http import HttpResponse
from .models import Mercury
from django.db.models import Sum, Avg, Min, Max
from .forms import StudentForm

# Create your views here.
"""def jupiter(request):
    data = Mercury.objects.all()
    return render(request, 'first.html', context={'data': data})

"""
def jupiter(request):
    mainList = []
    for i in range(1,11):
        x = Mercury.objects.all().filter(standard = i)
        s = Mercury.objects.filter(standard = i).aggregate(Sum('marks'))
        z = Mercury.objects.all().filter(standard = i).aggregate(Max('marks'))
        t_list = Mercury.objects.all().filter(standard=i,marks=z['marks__max'])
        avg_list = Mercury.objects.all().filter(standard=i).aggregate(Avg('marks'))
        min_list = Mercury.objects.all().filter(standard=i).aggregate(Min('marks'))
        m_list = Mercury.objects.all().filter(standard=i,marks=min_list['marks__min'])
        y = [x, z, i, t_list, s, avg_list, min_list, m_list]
        mainList.append(y)

    return render(request, 'first.html', context={'mainList': mainList})

def earth(request):
    if request.method == 'POST':
        student_form = StudentForm(data = request.POST)
        #print(student_form)
        if student_form.is_valid():
            student = student_form.save()
            print(student)
            student.save()
            #student_form = StudentForm()
            return render(request, 'thankyou.html', context={'student':student})
        else:
            print('form is not valid')
    else:
        student_form = StudentForm()

    return render(request, 'forms.html', context={'student_form':student_form})
