from django.db import models


# Create your models here.
class FieldWorker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    FUNCTIONS = (
        ('Harvest', 'Harvest'),
        ('Pruning', 'Pruning'),
        ('Scouting', 'Scouting'),
        ('Other', 'Other'),
    )
    function = models.CharField(max_length=8, choices=FUNCTIONS)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.first_name
