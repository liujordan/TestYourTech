from django.db import models
COMPUTER_TYPES = [('mac', 'MAC'), ('win', 'WIN')]
class SystemVariable(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    value = models.CharField(max_length=256)
    def __str__(self):
        return self.name
