from django.shortcuts import render, redirect
from django.http import JsonResponse


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


def praise_or_criticize(request):
    try:
        tno = int(request.GET.get('tno'))
        teacher = TbTeacher.objects.get(no=tno)
        if request.path.startswith('/praise'):
            teacher.gcount += 1
            count = teacher.gcount
        else:
            teacher.bcount += 1
            count = teacher.bcount
        teacher.save()
        data = {'code': 20000, 'msg': '操作成功', 'count': count}
    except (ValueError, TbTeacher.DoesNotExist):
        data = {'code': 20001, 'msg': '操作失败'}
    return JsonResponse(data)


def login(request):
    hint = ''
    return render(request, 'login.html', {'hint': hint})
