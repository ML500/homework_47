from django.db import models

STATUS_CHOICES = [('new', 'New'),
                  ('in_progress', 'In proccess'),
                  ('done', 'Done')]


class Goal(models.Model):
    describe = models.CharField(max_length=3000, null=False, blank=False, verbose_name='Description')
    detail = models.TextField(max_length=3000, null=True, blank=True, default='no description', verbose_name='Detail')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES, default='new', verbose_name='Status')
    execute_at = models.DateField(null=True, blank=True, default=None, verbose_name='Date of execution')

    def __str__(self):
        return "{}, {}, {}, {}".format(self.pk, self.describe, self.status, self.detail, self.execute_at)

    class Meta():
        verbose_name = 'Goal'
        verbose_name_plural = 'Goals'
