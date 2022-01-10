from django import forms
from .models import Program, Class, Topic, Lesson
from django.core.exceptions import ObjectDoesNotExist


class ProgramCreateForm(forms.Form):
    def clean_program_code(self):
        program_code = self.cleaned_data['program_code']
        try:
            Program.objects.get(program_code=program_code)
        except ObjectDoesNotExist:
            return program_code
        data = 'Chương trình ' + program_code + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = Program
        fields = '__all__'


class ClassCreateForm(forms.Form):
    def clean_class_code(self):
        class_code = self.cleaned_data['class_code']
        try:
            Class.objects.get(class_code=class_code)
        except ObjectDoesNotExist:
            return class_code
        data = 'Lớp ' + class_code + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = Class
        fields = '__all__'


class TopicCreateForm(forms.Form):
    def clean_topic_code(self):
        topic_code = self.cleaned_data['topic_code']
        try:
            Topic.objects.get(topic_code=topic_code)
        except ObjectDoesNotExist:
            return topic_code
        data = 'Môn ' + topic_code + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = Topic
        fields = '__all__'


class LessonCreateForm(forms.Form):
    def clean_lesson_code(self):
        lesson_code = self.cleaned_data['lesson_code']
        try:
            Lesson.objects.get(lesson_code=lesson_code)
        except ObjectDoesNotExist:
            return lesson_code
        data = 'Bài ' + lesson_code + ' đã tồn tại!'
        raise forms.ValidationError(data)

    class Meta:
        model = Lesson
        fields = '__all__'
