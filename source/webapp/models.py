from django.db import models


class Goal(models.Model):
    describe = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Description')
    status = models.CharField(max_length=40, null=False, blank=False, default='new', verbose_name='Status')
    execute_at = models.DateField(null=True, blank=True, default=None, verbose_name='Date of execution')

    def __str__(self):
        return "{}, {}, {}, {}".format(self.pk, self.describe, self.status, self.execute_at)

    class Meta():
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'
