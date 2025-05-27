from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from apis.serializer import  StoresSerializer, PoiSerializer, QuizSerializer, QuestionSerializer, RewardSerializer
from rest_framework.views import APIView

from .models import POI, Quiz, Question, Reward, Stores


class PoiViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = POI.objects.all()
    serializer_class = PoiSerializer

class QuizViewSet(mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def retrieve(self, request, *args, **kwargs):
        poi = POI.objects.get(id=kwargs['pk'])
        quiz = Quiz.objects.get(poi=poi)

        questions = quiz.questions.all().order_by('?')[:4]
        questions_serializer = QuestionSerializer(questions, many=True)
        return Response({
            'questions': questions_serializer.data
        })

class RewardViewSet(APIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer 

    def get(self, request):
        reward = Reward.objects.filter(is_active=True).all().order_by('?').first()

        if not reward:
            return Response({"message": "No active rewards found"}, status=404)
        reward.is_active = False  
        reward.save()  

        serializer = RewardSerializer(reward)  
        return Response(serializer.data)

class StoreViewSet(mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer


