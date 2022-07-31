from django.shortcuts import render
from eduApp.backend.study_program.models import Program, Class, Lesson, Topic
from django.views.decorators.http import require_http_methods
from eduApp.backend.about_us.models import About

all_program = Program.objects.filter(program_status=True)


@require_http_methods(["GET"])
def index(request):
    if request.method == 'GET':
        obj_program = Program.objects.filter(program_status=True).order_by('program_stt')
        obj_lesson = Lesson.objects.filter(lesson_status=True).order_by('-lesson_id')[:12]
        return render(request, 'index.html', {'obj_program': obj_program, 'all_program': all_program, 'obj_lesson': obj_lesson})


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
        return render(request, 'online-learning.html', {
            'all_program': all_program})


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
        return render(request, 'lesson.html', {
            'lesson_id': lesson_id,
            'new_lesson': new_lesson,
            'obj_topic': obj_topic,
            'obj_class': obj_class,
            'obj_lesson': obj_lesson,
            'obj_program': obj_program,
            'all_program': all_program
        })


@require_http_methods(["GET"])
def login_client(request):
    if request.method == 'GET':
        return render(request, 'login-client.html')


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
