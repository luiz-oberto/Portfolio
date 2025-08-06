import uuid
from django.db import models

class Visitante(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50)
    data_entrada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} ({self.id})'
