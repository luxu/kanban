from django.db import models


class Fields(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=20,
        choices=(
            ('text', 'Text'),
            ('textarea', 'Textarea'),
            ('number', 'Number'),
            ('date', 'Date'),
            ('checkbox', 'Checkbox'),
            ('select', 'Select'),
            ('radio', 'Radio'),
            ('file', 'File'),
            ('image', 'Image'),
        )
    )
    attributes = models.JSONField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Field: {self.name} - {self.type}'


class Cards(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    phase = models.ForeignKey('Phases', on_delete=models.CASCADE, related_name='cards')

    @property
    def name_fase(self):
        return f'Fase: {self.phase.id} - {self.phase.name}' if self.phase else self.phase.name

    def __str__(self):
        return f'Card: {self.title}'


class CardFields(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.CASCADE)
    field = models.ForeignKey(Fields, on_delete=models.CASCADE)

    def __str__(self):
        return f'CardField: {self.card} - {self.field}'


class CardFieldValues(models.Model):
    card = models.ForeignKey(Cards, on_delete=models.CASCADE, related_name='cards')
    field = models.ForeignKey(Fields, on_delete=models.CASCADE, related_name='fields')
    value = models.TextField()

    def __str__(self):
        return f'Card: {self.card} - Field: {self.field} - Value: {self.value}'


class Phases(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'Phase: {self.name}'
