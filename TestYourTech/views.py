from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from selenium import webdriver
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import os
from .models import *
from .serializers import *
from Variables.models import SystemVariable
from django.utils.decorators import method_decorator
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def _execute(browser, function, selector=None, value=None):
    def click(browser1, selector1, value1=None):
        try:
            element = WebDriverWait(browser1, 10).until(
                EC.presence_of_element_located((By.XPATH, selector1))
            )
            element.click()
        except:
            print("timedout", function, selector1, value1)
    def submit(browser1, selector1, value1=None):
        try:
            element = WebDriverWait(browser1, 10).until(
                EC.presence_of_element_located((By.XPATH, selector1))
            )
            element.submit()
        except:
            print("timedout", function, selector1, value1)
    def mytype(browser1, selector1, value1):
        try:
            element = WebDriverWait(browser1, 10).until(
                EC.presence_of_element_located((By.XPATH, selector1))
            )
            element.send_keys(value)
        except:
            print("timedout", function, selector1, value1)
    def open_url(browser1, selector1, value1):
        browser.get(value)
    if function == 'click':
        function = click
    elif function == 'type':
        function = mytype
    elif function == 'url':
        function = open_url
    elif function == 'submit':
        function = submit
    return function(browser, selector, value)
def _validate(browser, selector, value):
    if not value:
        print("Result validate value not set")
        return True
    element = WebDriverWait(browser1, 10).until(
        EC.presence_of_element_located((By.XPATH, selector1))
    )
    return element.text == value
@csrf_exempt
def runView(request):
    if request.method == 'POST':
        message = ""
        # initiate the browser
        webdriver_dir = SystemVariable.objects.get(pk='webdriver_dir').value
        computer_type = SystemVariable.objects.get(pk='computer_type').value
        # initiate the actions
        try:
            action = Action.objects.get(id=int(request.POST.get("action_id", 0)))
        except Action.DoesNotExist:
            return HttpResponse(status=404)
        browser = webdriver.Chrome(os.path.join(os.path.join(webdriver_dir, computer_type), "chromedriver.exe"))
        while True:
            print("Action now: ", action.name)
            function = action.action_type
            selector = action.selector
            value = action.value
            _execute(browser, function, selector, value)

            if _validate(browser, action.result.selector, action.result.value):
                message += action.name + ": Success\n"
            else:
                message += action.name + ": Fail\n"
            try:
                new_id = ActionLink.objects.get(this=action.id).after.id
                action = Action.objects.get(id=new_id)
            except:
                break
        browser.quit()
        if message:
            return HttpResponse(message)
        return HttpResponse('Ran test without errors')

class runTestView(View):
    def get(self, request):
        action = Action.objects.get(id=int(request.GET["action_id"]))
        print(action)
        browser = webdriver.Chrome('webdrivers/mac/chromedriver');
        while action is not None:
            if action.action_type == "url":
                browser.get(action.selector.value)
            elif action.action_type == "type":
                # example for string
                if action.selector.selector_type == "string":
                    elem = browser.find_element_by_name(action.selector.value)
                    elem.send_keys(action.name)
                    elem.submit()
            elif action.action_type == "click":
                pass
            # temp ignore other actions, only consider linear actions
            next_actions = action.next_action.get_queryset()
            try:
                action = next_actions[0]
            except IndexError:
                action = None
        # quit browser after completing test
        browser.quit()
        return HttpResponse("ran test without errors")

def model_list(request, Model, ModelSerializer):
    if request.method == 'GET':
        model = Model.objects.all()
        serializer = ModelSerializer(model, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        pprint(request.POST)
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
@csrf_exempt
def action_link_list(request):
    return model_list(request, ActionLink, ActionLinkSerializer)
@csrf_exempt
def action_link_detail(request, pk):
    return model_detail(request, pk, ActionLink, ActionLinkSerializer)
@csrf_exempt
def action_result_list(request, action_pk):
    try:
        action = Action(pk=action_pk)
    except Action.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        result = action.results.all()
        serializer = ResultSerializer(result, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ResultSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            action.add(Result(pk=serializer.data['id']))
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class ActionView2(View):

    # view
    def get(self, request):
        action = Action.objects.get(id=request.POST["action_id"])

    def post(self, request):
        print(request.POST)
        action = Action.objects.get(id=int(request.POST["action_id"]))
        action.name = request.POST["name"]
        action.action_type = request.POST["action_type"]
        action.selector = request.POST["action_selector"]
        action.value = request.POST["selector_value"]
        action.left_pos = request.POST["left_pos"]
        action.top_pos = request.POST["top_pos"]
        action.save()

        return HttpResponse(status=200)


@csrf_exempt
def action_result_detail(request, action_pk, result_pk):
    try:
        action = Action(pk=action_pk)
    except Action.DoesNotExist:
        return HttpResponse(status=404)
    try:
        result = action.results.get(pk=result_pk)
    except Result.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ResultSerializer(result)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ResultSerializer(result, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        result.delete()
        return HttpResponse(status=204)
class HomeView(TemplateView):
    template_name = 'TestYourTech/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['action_types'] = ACTION_TYPES;
        # context['selector_types'] = SELECTOR_TYPES;
        context['first_action'] = Action.objects.get(id=1)
        context['actions'] = Action.objects.all()
        return context
