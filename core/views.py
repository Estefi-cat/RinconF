from django.shortcuts import render, HttpResponse
html_base="""
<h1>Rincón Floreciente</h1>
<ul>
    <li><a href ="/">Pagina Principal</a></li>
    <li><a href ="/flowers">Tipos de Flores</a></li>
    <li><a href ="/history"</a>Tus historias de Flores</li>
    <li><a href ="/contact"</a>Contacto</li>
</ul>
"""

# Create your views here.
def home (request):
    return render(request,"core/home.html")


def flowers (request):
    return render(request,"core/flowers.html")


def contact (request):
    return render(request,"core/contact.html") 
