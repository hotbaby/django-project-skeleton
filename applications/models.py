# encoding: utf8

from django.db import models


class BaseModel(models.Model):
    class Meta:
        abstract = True

    state = models.IntegerField(default=1, help_text='物理状态')
    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间')
