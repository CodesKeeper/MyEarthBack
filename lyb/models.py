from django.db import models


class Lyb(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    content = models.TextField()
    posttime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "d_lyb"


class Student(models.Model):
    # 模型字段
    name = models.CharField(max_length=100, verbose_name="姓名")
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
    class_null = models.CharField(max_length=5, verbose_name="班级编号")
    description = models.TextField(max_length=1000, verbose_name="个性签名")

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name
