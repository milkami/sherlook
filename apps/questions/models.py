from django.db import models


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField(blank=True, null=True)
    answer = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
