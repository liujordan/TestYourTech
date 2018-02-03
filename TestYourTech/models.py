from django.db import models
ACTION_TYPES = [
	('click', 'CLICK'),
	('type', 'TYPE')]
class Action(models.Model):
	id = models.IntegerField()
	type = models.CharField(max_length=256, choices=ACTION_TYPES, default='click')
	selector = models.ForeignKey(Selector, on_delete=models.CASCADE)
	name = models.CharField(max_length=256)
	testcases = models.ManyToManyField(
		TestCase,
		through='TestCaseLink',
		through_fields=('action', 'testcase'))
	results = models.ManyToManyField(
		Result,
		through='ResultLink',
		through_fields=('action', 'result'))
	action_link = models.ManyToManyField(
		Action,
		through='ActionLink',
		through_fields=('action', 'next_action'))
class Result(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=256)
	selector = models.ForeignKey(Selector, on_delete=models.CASECADE)
	
class TestCase(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=256)
class ActionLink(models.Model):
	action = models.ForeignKey(Action, on_delete=models.CASCADE)
	next_action = models.ForeignKey(Action, on_delete=models.CASCADE)
class ResultLink(models.Model):
	action = models.ForeignKey(Action, on_delete=models.CASCADE)
	result = models.ForeignKey(Result, on_delete=models.CASCADE)
class TestCaseLink(models.Model):
	action = models.ForeignKey(Action, on_delete=models.CASCADE)
	testcase = models.ForeignKey(TestCase, on_delete=models.CASCADE)
