from django.db import models

class djangoClasses(models.Model):
    title = models.CharField(max_length=255, default='', blank=True, null=False)
    courseNumber = models.IntegerField(default='')
    instructorName = models.CharField(max_length=50, default='')
    studentName = models.CharField(max_length=50, default='')
    duration = models.FloatField(max_length=2, default='')
    doesPass = models.BooleanField(default=False)
    isBehind = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.title