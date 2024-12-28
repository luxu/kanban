from rest_framework import serializers
from .models import Phases, Cards, Fields

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Cards
        fields = ['id', 'title', 'phase', 'name_fase', 'created_at', 'fields']

class PhaseSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = Phases
        fields = "__all__"
