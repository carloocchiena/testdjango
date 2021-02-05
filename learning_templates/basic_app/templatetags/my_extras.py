#ci serve questa pagina per usare le funzioni filtro custom (create da noi, non quelle standard) sui tag html.
#questa pagina va poi passata nell'header dell'html dove tali filtri avranno impatto  es {% load my_extras %}


from django import template
register = template.Library()

@register.filter
def cutout(value, arg):
    return value.replace(arg, '')
