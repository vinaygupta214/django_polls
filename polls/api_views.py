#class based View

from rest_framework import generics,viewsets
from .models import Question,Choice
from .serializers import QuestionSerializer,ChoiceSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination

class QuestionPagination(PageNumberPagination):
    page_size = 5

class QuestionList(generics.ListCreateAPIView):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]
    pagination_class=QuestionPagination

    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class=QuestionSerializer 

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class=ChoiceSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]       