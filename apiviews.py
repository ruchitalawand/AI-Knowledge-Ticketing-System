from rest_framework import viewsets
from articles.models import Article
from tickets.models import Ticket
from api.serializers import ArticleSerializer, TicketSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
