from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, redirect
from .models import Card
from .forms import CardForm
from django.core.files.base import ContentFile
import base64


@login_required(login_url='login')
@require_http_methods(["GET"])
def index(request):
    obj_card = Card.objects.all()
    return render(request, 'card/index_card.html', {'obj_card': obj_card})


@login_required(login_url='login')
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == 'GET':
        card_form = CardForm()
        return render(request, 'card/create.html', {
            'card_form': card_form
        })
    else:
        obj_card = Card()
        card_name = request.POST['card_name']
        card_price = request.POST['card_price']
        card_photo = ''
        if len(request.FILES) != 0:
            photo = request.FILES.get('photo')
            card_photo = 'card_images/' + photo.name
            fs = FileSystemStorage()
            filename = fs.save(card_photo, photo)
            card_photo = fs.url(filename)

        obj_card.card_image = card_photo
        obj_card.card_name = card_name
        obj_card.card_price = card_price
        obj_card.save()
        return redirect('card:index')
