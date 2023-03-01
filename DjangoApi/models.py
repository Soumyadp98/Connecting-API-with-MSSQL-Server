from django.db import models

class sqlserverconn(models.Model):
    SLNO=models.IntegerField()
    SPIRITUAL_HEADING=models.CharField(max_length=100)
    SPIRITUAL_TEXT=models.CharField(max_length=1000)
    CURR_DATE=models.DateField()
