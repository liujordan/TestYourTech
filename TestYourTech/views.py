from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from selenium import webdriver
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

class runView(View):
    def get(self, request):
        browser = webdriver.Chrome('C:\\Users\\Jordan Liu\\Desktop\\TestYourTech\\webdrivers\\win\\chromedriver.exe')
        browser.get('https://www.google.ca')
        elem = browser.find_element_by_name('q')
        elem.send_keys('how to google')
        elem.submit()
        browser.quit()
        return HttpResponse('Ran test without errors')

def model_list(request, Model, ModelSerializer):
    if request.method == 'GET':
        model = Model.objects.all()
        serializer = ModelSerializer(model, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
def model_detail(request, pk, Model, ModelSerializer):
    try:
        model = Model.objects.get(pk=pk)
    except Model.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = ModelSerializer(model)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ModelSerializer(model, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        model.delete()
        return HttpResponse(status=204)
@csrf_exempt
def selector_list(request):
    return model_list(request, Selector, SelectorSerializer)
@csrf_exempt
def selector_detail(request, pk):
    return model_detail(request, pk, Selector, SelectorSerializer)
@csrf_exempt
def testcase_list(request):
    return model_list(request, TestCase, TestCaseSerializer)
@csrf_exempt
def testcase_detail(request, pk):
    return model_detail(request, pk, TestCase, TestCaseSerializer)
@csrf_exempt
def result_list(request):
    return model_list(request, Result, ResultSerializer)
@csrf_exempt
def result_detail(request, pk):
    return model_detail(request, pk, Result, ResultSerializer)
@csrf_exempt
def action_list(request):
    return model_list(request, Action, ActionSerializer)
@csrf_exempt
def action_detail(request, pk):
    return model_detail(request, pk, Action, ActionSerializer)
class HomeView(TemplateView):
    template_name = 'TestYourTech/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['action_types'] = ACTION_TYPES;
        # context['selector_types'] = SELECTOR_TYPES;
        return context
