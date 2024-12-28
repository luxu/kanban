from django.contrib import admin
from .models import Phases, Fields, Cards, CardFieldValues

@admin.register(Phases)
class PhaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Fields)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', )
    list_filter = ('type',)

@admin.register(Cards)
class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'phase', 'created_at')
    list_filter = ('phase',)

@admin.register(CardFieldValues)
class CardFieldValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'card', 'field', 'value')
    list_filter = ('field',)
