from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpRequest, HttpResponse


from polls.models import TbSubject, TbTeacher, User

from polls import utils

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


def praise_or_criticize(request: HttpRequest) -> HttpResponse:
    if request.session.get('userid'):
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
    else:
        data = {'code': 20002, 'msg': '请先登录'}
    return JsonResponse(data)


def login(request: HttpRequest) -> HttpResponse:
    hint = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            password = utils.gen_md5_digest(password)
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['userid'] = user.no
                request.session['username'] = user.username
                return redirect('/')
            else:
                hint = '用户名密码错误'
        else:
            hint = '请输入有效的用户名和密码'
    return render(request, 'login.html', {'hint': hint})


def get_captcha(request):
    """验证码"""
    captcha_text = utils.gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = utils.Captcha.instance().generate(captcha_text)


def logout(request):
    """注销"""
    request.session.flush()
    return redirect('/')

