from django.db import models
ACTION_TYPES = [
	('click', 'CLICK'),
	('type', 'TYPE')]
class Action(models.Model):
	id = models.IntegerField()
	type = models.CharField(max_length=256, choices=ACTION_TYPES, default='click')
	selector = models.OneToOneField(
		Selector,
		on_delete=models.CASCADE,
		primary_key=True),
	action_name = models.CharField(max_length)
	results = models.ManyToMany
	action_link = models.ManyToManyField(
		Action,
		through='ActionLink',
		through_fields=('action', 'next_action'),
	)


class ActionLink(models.Model):
	action = models.ForeignKey(Action, on_delete=models.CASCADE)
	next_action = models.ForeignKey(Action, on_delete=models.CASCADE)
