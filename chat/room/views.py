# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'room/index.html'


class ChatRoomView(TemplateView):
    template_name = 'room/room.html'

