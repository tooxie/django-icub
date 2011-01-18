from django.template import Library, Node
from menu.models import Menu, Link

register = Library()

class MenuNode(Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        #TODO: permitir subitems.
        """
        item['valor'] = ""
        item['hijo'] = ""
        item['hermano'] = ""
        menu = Menu.objects.get(nombre=menu_name)
        #links = Link.objects.filter(menu=menu)
        for link in menu.link.all():
            item['valor'] = link
            item['hijo'] = ""
            item['hermano'] = ""
            link = item
        context['menu'] = ""
        """
        try:
            html = '<ul class="%s">' % (self.menu_name)
            menu = Menu.objects.get(nombre=self.menu_name)
            for link in menu.links.filter(desactivar=False):
                html += '<li><a href="%s" title="%s">%s</a></li>' % (link.href, link.nombre, link.nombre)
            html += '</ul>'
        except:
            html = ""
        #context['menu'] = "a"
        return html

def render_menu(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "render_menu solo recibe un argumento, el nombre del menu."
    return MenuNode(bits[1])

menu = register.tag(render_menu)
