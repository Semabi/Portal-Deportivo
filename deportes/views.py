from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Portal Deportivo</h1><p>Bienvenido a la red más grande de noticias deportivas.</p>")

def futbol(request):
    return HttpResponse("<h1>Sección de Fútbol</h1><p>¡Hola! Aquí encontrarás los resultados de la jornada y tablas de posiciones.</p>")

def baloncesto(request):
    return HttpResponse("<h1>Sección de Baloncesto</h1><p>Saludos aficionado. Sigue de cerca los playoffs y estadísticas.</p>")

def tenis(request):
    return HttpResponse("<h1>Sección de Tenis</h1><p>¡Qué tal! Entérate de los últimos campeones del Grand Slam.</p>")

def natacion(request):
    return HttpResponse("<h1>Sección de Natación</h1><p>Hola, revisa los nuevos récords mundiales y tiempos de competición.</p>")