from django.views.generic import ListView
from .models import GamesNews

class GameNewsListView(ListView):
    model = GamesNews
    template_name = 'GameNews/GameNews/lista_news.html'
    context_object_name = 'GameNews'