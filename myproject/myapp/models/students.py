from django.db import models

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70)

    class Meta:
        # managed = False
        db_table = 'students'
    
