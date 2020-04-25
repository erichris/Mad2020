from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .models import ModulesPrice
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import MyForm


def index(request):
    if request.user.is_authenticated:

        template = loader.get_template('Prices.html')

        #CAJONERAS
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=False, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=False, typeOf="CAJONERA")

        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=False, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=False, typeOf="CAJONERA")

        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=True, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=False, typeOf="CAJONERA")
        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=False, typeOf="CAJONERA")

        #REPISEROS
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=False, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=False, typeOf="REPISERO")

        ModulesPrice.objects.get_or_create(size=.5, door=True, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.5, door=False, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.5, door=False, interiorBlanco=False, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.5, door=True, interiorBlanco=False, typeOf="REPISERO")

        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=False, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=False, typeOf="REPISERO")

        ModulesPrice.objects.get_or_create(size=.7, door=True, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.7, door=False, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.7, door=False, interiorBlanco=False, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.7, door=True, interiorBlanco=False, typeOf="REPISERO")

        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=True, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=False, typeOf="REPISERO")
        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=False, typeOf="REPISERO")

        #COLGADOR
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.4, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.4, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=.5, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.5, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.5, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.5, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.6, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.6, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=.7, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.7, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.7, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.7, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.8, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.8, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=.9, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.9, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.9, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=.9, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=1, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=1.1, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.1, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.1, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.1, door=True, interiorBlanco=False, typeOf="COLGADOR")

        ModulesPrice.objects.get_or_create(size=1.2, door=True, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.2, door=False, interiorBlanco=True, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.2, door=False, interiorBlanco=False, typeOf="COLGADOR")
        ModulesPrice.objects.get_or_create(size=1.2, door=True, interiorBlanco=False, typeOf="COLGADOR")


        context = {

            #CAJONERAS
            'CA1140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=True, typeOf="CAJONERA").price,
            'CA0040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=False, typeOf="CAJONERA").price,
            'CA0140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=False, typeOf="CAJONERA").price,
            'CA1040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=True, typeOf="CAJONERA").price,

            'CA1160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=True, typeOf="CAJONERA").price,
            'CA0060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=False, typeOf="CAJONERA").price,
            'CA1060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=True, typeOf="CAJONERA").price,
            'CA0160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=False, typeOf="CAJONERA").price,

            'CA1180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=True, typeOf="CAJONERA").price,
            'CA0080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=False, typeOf="CAJONERA").price,
            'CA1080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=True, typeOf="CAJONERA").price,
            'CA0180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=False, typeOf="CAJONERA").price,

            #REPISEROS
            'RE1140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=True, typeOf="REPISERO").price,
            'RE1040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=True, typeOf="REPISERO").price,
            'RE0040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=False, typeOf="REPISERO").price,
            'RE0140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=False, typeOf="REPISERO").price,

            'RE1150': ModulesPrice.objects.get(size=.5, door=True, interiorBlanco=True, typeOf="REPISERO").price,
            'RE1050': ModulesPrice.objects.get(size=.5, door=False, interiorBlanco=True, typeOf="REPISERO").price,
            'RE0050': ModulesPrice.objects.get(size=.5, door=False, interiorBlanco=False, typeOf="REPISERO").price,
            'RE0150': ModulesPrice.objects.get(size=.5, door=True, interiorBlanco=False, typeOf="REPISERO").price,

            'RE1160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=True, typeOf="REPISERO").price,
            'RE1060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=True, typeOf="REPISERO").price,
            'RE0060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=False, typeOf="REPISERO").price,
            'RE0160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=False, typeOf="REPISERO").price,

            'RE1170': ModulesPrice.objects.get(size=.7, door=True, interiorBlanco=True, typeOf="REPISERO").price,
            'RE1070': ModulesPrice.objects.get(size=.7, door=False, interiorBlanco=True, typeOf="REPISERO").price,
            'RE0070': ModulesPrice.objects.get(size=.7, door=False, interiorBlanco=False, typeOf="REPISERO").price,
            'RE0170': ModulesPrice.objects.get(size=.7, door=True, interiorBlanco=False, typeOf="REPISERO").price,

            'RE1180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=True, typeOf="REPISERO").price,
            'RE1080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=True, typeOf="REPISERO").price,
            'RE0080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=False, typeOf="REPISERO").price,
            'RE0180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=False, typeOf="REPISERO").price,


            #COLGADORES
            'CO1140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0040': ModulesPrice.objects.get(size=.4, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0140': ModulesPrice.objects.get(size=.4, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO1150': ModulesPrice.objects.get(size=.5, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1050': ModulesPrice.objects.get(size=.5, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0050': ModulesPrice.objects.get(size=.5, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0150': ModulesPrice.objects.get(size=.5, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO1160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0060': ModulesPrice.objects.get(size=.6, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0160': ModulesPrice.objects.get(size=.6, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO1170': ModulesPrice.objects.get(size=.7, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1070': ModulesPrice.objects.get(size=.7, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0070': ModulesPrice.objects.get(size=.7, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0170': ModulesPrice.objects.get(size=.7, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO1180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0080': ModulesPrice.objects.get(size=.8, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0180': ModulesPrice.objects.get(size=.8, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO1190': ModulesPrice.objects.get(size=.9, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO1090': ModulesPrice.objects.get(size=.9, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO0090': ModulesPrice.objects.get(size=.9, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO0190': ModulesPrice.objects.get(size=.9, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO11100': ModulesPrice.objects.get(size=1, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO10100': ModulesPrice.objects.get(size=1, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO00100': ModulesPrice.objects.get(size=1, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO01100': ModulesPrice.objects.get(size=1, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO11110': ModulesPrice.objects.get(size=1.1, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO10110': ModulesPrice.objects.get(size=1.1, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO00110': ModulesPrice.objects.get(size=1.1, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO01110': ModulesPrice.objects.get(size=1.1, door=True, interiorBlanco=False, typeOf="COLGADOR").price,

            'CO11120': ModulesPrice.objects.get(size=1.2, door=True, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO10120': ModulesPrice.objects.get(size=1.2, door=False, interiorBlanco=True, typeOf="COLGADOR").price,
            'CO00120': ModulesPrice.objects.get(size=1.2, door=False, interiorBlanco=False, typeOf="COLGADOR").price,
            'CO01120': ModulesPrice.objects.get(size=1.2, door=True, interiorBlanco=False, typeOf="COLGADOR").price,
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/admin/')


def update_price2(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MyForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, 'UpdatePrice.html', {'form': form})


def update_price(request):
    size = request.GET.get('size')
    door = request.GET.get('door')
    interiorBlanco = request.GET.get('interiorBlanco')
    typeOf = request.GET.get('typeOf')
    instance = ModulesPrice.objects.get(size=size, door=door, interiorBlanco=interiorBlanco, typeOf=typeOf)
    form = MyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('http://127.0.0.1:8000/')
    return render(request, 'UpdatePrice.html', {'form': form})

@csrf_exempt
def request_server(request):
    data = {"STATUS": 100}
    if request.method == 'POST':
        data = {"STATUS": 200}
        if request.POST.get('ACTION') == "CheckConnection":
            data = {"STATUS": 300}
            print("CheckConnection")
            #data = Login(request)
            data = {"STATUS": 300}
        elif request.POST.get('ACTION') == "GetPrice":
            data = {"STATUS": 300}
            print("GetPrice")
            print(request.POST )
            #data = Login(request)
            data = queryPrice(request)
    print(data)
    return JsonResponse(data, safe=False)

def queryPrice(request):
    HASDOOR = request.POST.get('HASDOOR')
    SIZE = request.POST.get('SIZE')
    MODULE = request.POST.get('MODULE')
    INTERIORBLANCO = request.POST.get('INTERIORBLANCO')
    print(HASDOOR)
    print(SIZE)
    print(MODULE)
    print(INTERIORBLANCO)
    obj = ModulesPrice.objects.get(size=SIZE, door=HASDOOR, interiorBlanco=INTERIORBLANCO, typeOf=MODULE)
    print (obj.price)
    return{"PRICE": obj.price}