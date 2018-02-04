from rest_framework import serializers
from .models import *
SELECTOR_TYPES = [
    ('id', 'ID'),
    ('css_selector', 'CSS_SELECTOR'),
    ('xpath', 'XPATH')]
class SelectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selector
        fields = '__all__'
class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = '__all__'
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
class ActionSerializer(serializers.ModelSerializer):
    testcases = TestCaseSerializer(many=True)
    results = ResultSerializer(many=True)
    class Meta:
        model = Action
        fields = '__all__'
class ActionLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionLink
        fields = '__all__'
ActionSerializer.next_action = ActionSerializer(many=True)
ResultSerializer.actions = ActionSerializer(many=True)
