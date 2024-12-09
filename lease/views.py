from django.shortcuts import render
from .models import Index, Slider, About, Service, Properties, Property_single, Contact, Agent, Testimonial


def about(request):
    about = About.objects.all()
    return render(request, 'about.html', {'about': about})

def index(request):
    index = Index.objects.all()
    slider = Slider.objects.all()
    properties_list = Properties.objects.all().prefetch_related('images')
    service = Service.objects.all()
    agent = Agent.objects.all()
    testimonial = Testimonial.objects.all()
    return render(request, 'index.html', {'index': index, 'sliders': slider, 'properties_list': properties_list, 'service' : service, 'agent':agent, 'testimonial' : testimonial })
    

def agents(request):
    agents = Agent.objects.all()
    return render(request, 'agents.html', {'agents': agents})

def properties(request):
    properties = Properties.objects.all().prefetch_related('images')
    return render(request, 'properties.html', {'properties': properties})

def property_single(request, pk):
    property = Properties.objects.prefetch_related('images').get(id=pk)
    return render(request, 'property-single.html', {'property': property})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

def testimonial(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'testimonial.html', {'testimonial': testimonial})



# Create your views here.
