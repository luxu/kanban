from rest_framework.viewsets import ModelViewSet

from .models import Phases, Cards, Fields
from .serializers import PhaseSerializer, CardSerializer, FieldSerializer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class PhaseViewSet(ModelViewSet):
    queryset = Phases.objects.prefetch_related("cards").all()
    serializer_class = PhaseSerializer

@method_decorator(csrf_exempt, name='dispatch')
class CardViewSet(ModelViewSet):
    queryset = Cards.objects.all()
    serializer_class = CardSerializer

class FieldViewSet(ModelViewSet):
    queryset = Fields.objects.all()
    serializer_class = FieldSerializer
