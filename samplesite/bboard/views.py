# Контроллер Django — это код, запускаемый при обращении по интернет-адресу
# определенного формата и в ответ выводящий на экран определенную веб-страницу.(viev - устаревшее)

from django.http import HttpResponse
from django.template import loader
from .models import Bd


def index(request):
    template = loader.get_template('bboard/index.html')
    bbs = Bd.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))
