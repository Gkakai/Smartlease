from django.shortcuts import render
from .models import Index, Slider, Properties_list, About, Services, Properties, Property_single, Contact, Agents


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')



def index(request):
    index = Index.objects.all()
    slider = Slider.objects.all()
    properties_list = Properties_list.objects.all() # Limit to 3 properties for homepage
    return render(request, 'index.html', {'index': index, 'sliders': slider, 'properties_list': properties_list})

def agents(request):
    agents = Agents.objects.all()
    return render(request, 'agents.html', {'agents': agents})

def properties(request):
    properties = Properties.objects.all()
    return render(request, 'properties.html', {'properties': properties})



def property_single(request, id):
    property = Property_single.objects.get(id=id)
    return render(request, 'property-single.html', {'property': property})

def services(request):
    services = Services.objects.all()
    return render(request, 'services.html', {'services': services})




# Create your views here.
