import datetime
from django.shortcuts import render, redirect

from eduApp.backend.client.models import UserClient
from eduApp.backend.study_program.models import Program, Class, Lesson, Topic
from django.views.decorators.http import require_http_methods
from eduApp.backend.about_us.models import About
from eduApp.backend.card.models import Card, History
from django.db.models import Q

all_program = Program.objects.filter(program_status=True)


@require_http_methods(["GET"])
def index(request):
    if request.method == 'GET':
        count_client = UserClient.objects.filter(client_status=True).count()
        obj_lesson = Lesson.objects.filter(lesson_status=True)
        obj_program = Program.objects.filter(program_status=True).order_by('program_stt')
        count_lesson = obj_lesson.count()
        list_lesson = obj_lesson.order_by('-lesson_id')[:12]
        return render(request, 'index.html',
                      {
                          'obj_lesson': list_lesson,
                          'obj_program': obj_program,
                          'all_program': all_program,
                          'count_lesson': count_lesson,
                          'count_client': count_client
                      })


@require_http_methods(["GET"])
def about(request):
    about_data = About.objects.filter(about_status=True)
    return render(request, 'about.html', {
        'about_data': about_data,
        'all_program': all_program
    })


@require_http_methods(["GET"])
def program(request, program_id):
    if request.method == 'GET':
        obj = Class.objects.filter(class_program_id=program_id)
        obj_program = Program.objects.get(program_id=program_id)
        return render(request, 'program.html', {
            'obj': obj,
            'program': obj_program,
            'program_id': program_id,
            'all_program': all_program
        })


@require_http_methods(["GET"])
def cls(request, class_id):
    if request.method == 'GET':
        obj_class = Class.objects.get(class_id=class_id)
        obj_topic = Topic.objects.filter(topic_class_id=class_id)
        obj_program = Program.objects.get(program_id=obj_class.class_program_id)
        return render(request, 'class.html', {
            'class_id': class_id,
            'obj_topic': obj_topic,
            'obj_class': obj_class,
            'obj_program': obj_program,
            'all_program': all_program
        })


@require_http_methods(["GET"])
def topic(request, topic_id):
    if request.method == 'GET':
        stt = 0
        obj_topic = Topic.objects.get(topic_id=topic_id)
        obj_class = Class.objects.get(class_id=obj_topic.topic_class_id)
        obj_program = Program.objects.get(program_id=obj_class.class_program_id)
        obj_lesson = Lesson.objects.filter(lesson_status=True, lesson_topic_id=topic_id)
        for i in obj_lesson:
            stt = stt + 1
            i.stt = stt
        return render(request, 'topic.html', {
            'topic_id': topic_id,
            'obj_topic': obj_topic,
            'obj_class': obj_class,
            'obj_lesson': obj_lesson,
            'obj_program': obj_program,
            'all_program': all_program
        })


@require_http_methods(["GET"])
def learning(request):
    if request.method == 'GET':
        obj_card = Card.objects.all()
        return render(request, 'online-learning.html', {'obj_card': obj_card})


@require_http_methods(["GET"])
def learning_detail(request, card_id):
    if request.method == 'GET':
        obj_card = Card.objects.filter(pk=card_id)
        obj_all_card = Card.objects.filter(~Q(pk=card_id))
        print(obj_all_card)
        return render(request, 'online-learning-detail.html', {
            'obj_card': obj_card,
            'obj_all_card': obj_all_card
        })



@require_http_methods(["GET"])
def sell_card(request):
    if request.method == 'GET':
        return render(request, 'sell-card/card-product.html')


@require_http_methods(["GET"])
def lesson(request, lesson_id):
    if request.method == 'GET':
        obj_lesson = Lesson.objects.get(lesson_id=lesson_id)
        obj_topic = Topic.objects.get(topic_id=obj_lesson.lesson_topic_id)
        obj_class = Class.objects.get(class_id=obj_topic.topic_class_id)
        obj_program = Program.objects.get(program_id=obj_class.class_program_id)
        new_lesson = Lesson.objects.filter(lesson_status=True, lesson_topic_id=obj_lesson.lesson_topic_id).exclude(
            lesson_id=lesson_id)[:20]
        check = History.objects.filter(history_name=obj_lesson.lesson_name, history_user_id=request.session.get('user_id'), history_date=datetime.date.today())
        if check.count() == 0:
            obj_history = History()
            obj_history.history_date = datetime.date.today()
            obj_history.history_user_id = request.session.get('user_id')
            obj_history.history_name = obj_lesson.lesson_name
            obj_history.save()
        return render(request, 'lesson.html', {
            'lesson_id': lesson_id,
            'new_lesson': new_lesson,
            'obj_topic': obj_topic,
            'obj_class': obj_class,
            'obj_lesson': obj_lesson,
            'obj_program': obj_program,
            'all_program': all_program
        })


@require_http_methods(["GET", "POST"])
def login_client(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = UserClient.objects.filter(client_name=username, client_password=password)
        if client.count() > 0:
            first = client.first()
            if first.client_status == 0:
                first.client_status = 1
                first.client_start_date = datetime.date.today()
                first.client_end_date = datetime.date.today() + datetime.timedelta(days=365)
                first.save()
                request.session['user_id'] = first.client_id
                request.session['username'] = first.client_name
                return redirect('frontend:index')
            else:
                if first.client_end_date > datetime.date.today():
                    request.session['user_id'] = first.client_id
                    request.session['username'] = first.client_name
                    return redirect('frontend:index')
        else:
            return render(request, 'login-client.html', {
                'error': 'Tên đăng nhập hoặc mật khẩu không đúng'
            })

    return render(request, 'login-client.html')


@require_http_methods(["GET"])
def logout_client(request):
    if request.session.get('user_id') is not None:
        del request.session['user_id']
    if request.session.get('username') is not None:
        del request.session['username']
    return render(request, 'login-client.html', {'all_program': all_program})


@require_http_methods(["GET", "POST"])
def setting_client(request, client_id):
    client = UserClient.objects.get(client_id=client_id)
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        address = request.POST.get('address')
        client.client_mail = email
        client.client_name = username
        client.client_address = address
        client.save()
        request.session['username'] = username
        return render(request, 'setting-client.html',
                      {
                          'status': 'Cập nhật thành công',
                          'all_program': all_program,
                          'client': client
                      })
    return render(request, 'setting-client.html', {'all_program': all_program, 'client': client})


@require_http_methods(["GET", "POST"])
def change_password(request, client_id):
    client = UserClient.objects.get(client_id=client_id)
    if request.method == 'POST':
        re_password = request.POST.get('re-password')
        if re_password == client.client_password:
            password = request.POST.get('password')
            password_again = request.POST.get('password-again')
            if password == password_again:
                client.client_password = password
                client.save()
                return render(request, 'change-password.html',
                              {
                                  'status': 'Cập nhật thành công',
                                  'all_program': all_program,
                                  'client': client
                              })
            else:
                return render(request, 'change-password.html',
                              {
                                  'status': 'Vui lòng nhập lại mật khẩu',
                                  'all_program': all_program,
                                  'client': client
                              })
        else:
            return render(request, 'change-password.html',
                          {
                              'status': 'Mật khẩu cũ không đúng',
                              'all_program': all_program,
                              'client': client
                          })
    else:
        return render(request, 'change-password.html', {'all_program': all_program, 'client': client})


@require_http_methods(["GET", "POST"])
def history(request, client_id):
    obj = History.objects.filter(history_user_id=client_id, history_date=datetime.date.today())
    return render(request, 'history.html', {'obj': obj})


@require_http_methods(["GET"])
def login_instructions(request):
    if request.method == 'GET':
        return render(request, 'login-instructions.html')


@require_http_methods(["GET"])
def contact(request):
    if request.method == 'GET':
        return render(request, 'contact.html')


@require_http_methods(["GET"])
def service(request):
    if request.method == 'GET':
        return render(request, 'service.html', {'all_program': all_program})


@require_http_methods(["GET"])
def search(request):
    if request.method == 'GET':
        return render(request, 'search.html')
