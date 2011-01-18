from django.contrib.flatpages.models import FlatPage
from decorators import render_response
to_response = render_response('home/')

# Create your views here.
@to_response
def index(request):
    try:
        noticias = FlatPage.objects.get(title='inicio-noticias').content
    except:
        noticias = ''
    try:
        cursos = FlatPage.objects.get(title='inicio-cursos').content
    except:
        cursos = ''
    try:
        certificaciones = FlatPage.objects.get(title='inicio-certificaciones').content
    except:
        certificaciones = ''
    try:
        biblioteca = FlatPage.objects.get(title='inicio-biblioteca').content
    except:
        biblioteca = ''
    return 'home.html', { 'noticias': noticias, 'cursos': cursos, 'certificaciones': certificaciones, 'biblioteca': biblioteca }
