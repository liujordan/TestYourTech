from django.db import models
ACTION_TYPES = [
    ('click', 'CLICK'),
    ('type', 'TYPE'),
    ('url', 'GO TO URL')]
SELECTOR_TYPES = [
    ('id', 'ID'),
    ('css_selector', 'CSS_SELECTOR'),
    ('xpath', 'XPATH'),
    ('string', 'STRING')]


class Selector(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=256)
    selector_type = models.CharField(max_length=256, choices=SELECTOR_TYPES)
    value = models.CharField(max_length=256)


class TestCase(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=256)


class Result(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=256)
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)


class Action(models.Model):
    def __str__(self):
        return self.name
    action_type = models.CharField(max_length=256, choices=ACTION_TYPES, default='click')
    selector = models.ForeignKey(Selector, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    testcases = models.ManyToManyField(
        TestCase,
        blank=True)
    results = models.ManyToManyField(
        Result,
        blank=True)
    next_action = models.ManyToManyField(
        'self',
        blank=True)
