# arquitectura/views.py
from __future__ import annotations

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Nota


def home(request: HttpRequest) -> HttpResponse:
    """
    Página mínima: demuestra URL -> View -> Template.
    """
    contexto = {
        "titulo": "Explorador de arquitectura Django",
        "ruta": request.path,
        "metodo": request.method,
    }
    return render(request, "arquitectura/home.html", contexto)


def flujo(request: HttpRequest) -> HttpResponse:
    """
    Página para observar el flujo: router -> view -> render -> template.
    """
    contexto = {
        "titulo": "Flujo URL → View → Template",
        "ruta": request.path,
        "resolver_match": getattr(request, "resolver_match", None),
        # Datos simples para for/if en templates
        "pasos": [
            "Llega una HTTP Request a Django",
            "El enrutador (urls.py) decide qué view ejecutar",
            "La view prepara un contexto (dict)",
            "render() combina template + contexto",
            "Se retorna una HTTP Response",
        ],
        "mostrar_extra": True,
    }
    return render(request, "arquitectura/flujo.html", contexto)


def mvc(request: HttpRequest) -> HttpResponse:
    """
    Demostración mínima del componente 'M' (Model) + 'T' (Template) + 'V' (View).
    """
    notas = Nota.objects.order_by("-creado_en")[:10]
    contexto = {
        "titulo": "MTV (Model-Template-View) en mínimo",
        "notas": notas,
        "total_notas": Nota.objects.count(),
    }
    return render(request, "arquitectura/mvc.html", contexto)