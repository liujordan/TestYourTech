from django.db import models
ACTION_TYPES = [
	('click', 'CLICK'),
	('type', 'TYPE')]
class Action(models.Model):
	action_id = models.IntegerField()
	action_type = models.CharField(max_length=256, choices=ACTION_TYPES, default='click')
	selector = models.OneToOneField(
		Selector,
		on_delete=models.CASCADE,
		primary_key=True),
	action_name = models.CharField(max_length)
