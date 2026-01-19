# arquitectura/models.py
from __future__ import annotations

from django.db import models


class Nota(models.Model):
    """
    Modelo mínimo para evidenciar la capa 'M' (Model) en MTV.
    """

    titulo = models.CharField(max_length=120)
    contenido = models.TextField(blank=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        ordering = ["-creado_en"]

    def __str__(self) -> str:
        return self.titulo