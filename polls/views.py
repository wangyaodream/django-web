from django.shortcuts import render, redirect


from polls.models import TbSubject, TbTeacher

# Create your views here.


def show_subjects(request):
    subjects = TbSubject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = TbSubject.objects.only('name').get(no=sno)
            teachers = TbTeacher.objects.filter(sno=subject)
        else:
            subject = ""
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers})
    except (ValueError, TbSubject.DoesNotExist):
        return redirect('/')
