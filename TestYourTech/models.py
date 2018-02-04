from django.db import models
ACTION_TYPES = [
    ('click', 'CLICK'),
    ('type', 'TYPE'),
    ('url', 'GO TO URL'),
    ('submit', 'SUBMIT')]
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
    selector = models.CharField(max_length=256)
    value = models.CharField(max_length=256, blank=True)


class Action(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=256, blank=True)
    action_type = models.CharField(max_length=256, blank=True, choices=ACTION_TYPES, default='click')
    selector = models.CharField(max_length=256, blank=True) #ONLY XPATH
    value = models.CharField(max_length=256, blank=True, null=True)
    result = models.ForeignKey(Result, on_delete=models.CASCADE, null=True, blank=True)
    action_link = models.ManyToManyField('self', through='ActionLink', symmetrical=False)

class ActionLink(models.Model):
    def __str__(self):
        return self.this.name + ' to ' + self.after.name
    this = models.ForeignKey(Action, on_delete=models.CASCADE, related_name='current')
    after = models.ForeignKey(Action, on_delete=models.CASCADE)
