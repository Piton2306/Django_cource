# Контроллер Django — это код, запускаемый при обращении по интернет-адресу
# определенного формата и в ответ выводящий на экран определенную веб-страницу.(viev - устаревшее)

from django.http import HttpResponse
from .models import Bd


def index(request):
    s = 'Список объявлений\n\n\n'
    for bb in Bd.objects.order_by('-published'):
        s += bb.title + '\n' + bb.content + '\n\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
