from django.db import models


class SubjectList(models.Model):
    name = models.CharField(verbose_name='学科', max_length=64)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='最新修改时间', auto_now=True)

    def __str__(self):
        return self.name


class StudentList(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=64)
    sex_choices = (
        (1, '男'),
        (2, '女')
    )
    sex = models.IntegerField(verbose_name='性别', choices=sex_choices)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='最新修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Fraction(models.Model):
    student = models.ForeignKey(
        to='StudentList', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(
        to='SubjectList', to_field='id', on_delete=models.SET_NULL, null=True, blank=True)
    fraction = models.IntegerField(verbose_name='成绩')

