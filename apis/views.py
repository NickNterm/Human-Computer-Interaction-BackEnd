from rest_framework import (
    viewsets,
    mixins,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

from apis.serializer import  PoiSerializer, QuizSerializer, QuestionSerializer, RewardSerializer
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

class  RewardViewSet(APIView):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer 

    def get(self, request):
        reward = Reward.objects.filter(is_active=True).all().order_by('?').first()

        if not reward:
            return Response({"message": "No active rewards found"}, status=404)
        reward.is_active = False  # ✅ Modify the model instance
        reward.save()  # ✅ Save changes

        serializer = RewardSerializer(reward)  # ✅ Pass instance instead of data
        return Response(serializer.data)
    

## class GeneralSensorValuesViewSet(mixins.CreateModelMixin,
##                                  viewsets.GenericViewSet):
##     queryset = GeneralSensorValues.objects.all()
##     def create(self, request):
##         min = GeneralSensor.objects.get(id=request.data['sensor']).min_value
##         max = GeneralSensor.objects.get(id=request.data['sensor']).max_value
##         val = json.loads(request.data['data'])
##         val = float(val['value'])
##         if val < min or val > max:
##             serializer = PostGeneralSensorValuesSerializer(data=request.data)
##             serializer.is_valid(raise_exception=True)
##             serializer.save()
##             users = NotifiedUser.objects.all()
##             mails = []
##             for user in users:
##                 send_email(subject, body+"Value: "+str(val), sender, user.email, password)
## 
##             return Response({"message": "Value out of range, notifying Groups"})
## 
##         serializer = PostGeneralSensorValuesSerializer(data=request.data)
##         serializer.is_valid(raise_exception=True)
##         serializer.save()
## 
##         return Response(serializer.data)
##     def get_serializer_class(self):
##         if self.request.method == 'GET':
##             return GetGeneralSensorValuesSerializer
##         return PostGeneralSensorValuesSerializer
## 
## class GeneralSensorViewSet(mixins.ListModelMixin,
##                      mixins.CreateModelMixin,
##                      mixins.UpdateModelMixin,
##                      mixins.RetrieveModelMixin,
##                      viewsets.GenericViewSet):
##     queryset = GeneralSensor.objects.all()
##     http_method_names = ['get', 'post', 'put']
##     serializer_class =  GeneralSensorSerializer
## 
## 
## class WaterLevelSensorViewSet(mixins.ListModelMixin,
##                      mixins.CreateModelMixin,
##                      mixins.UpdateModelMixin,
##                      viewsets.GenericViewSet):
##     queryset = WaterLevelSensor.objects.all()
##     http_method_names = ['get', 'post', 'put']
##     serializer_class = WaterLevelSensorSerializer
