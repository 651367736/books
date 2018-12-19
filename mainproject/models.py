from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#管理员注册表
class AdminRegister(models.Model):
    a_id = models.AutoField(primary_key=True)
    a_name = models.CharField(max_length=30)
    a_pwd = models.CharField(max_length=30)
    a_sex = models.CharField(max_length=5)
    a_number = models.CharField(max_length=20)
    a_phone = models.CharField(max_length=15)


#职业表
class Professions(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=30)

#用户注册登录表
class UserRegister(models.Model):
    uid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=30)
    upwd = models.CharField(max_length=30)
    usex = models.CharField(max_length=5)
    unumber = models.CharField(max_length=20)
    uphone = models.CharField(max_length=15)
    bp_professions = models.ForeignKey(Professions) #和职业表的关系

#出版社表
class Press(models.Model):
    pr_id = models.AutoField(primary_key=True)
    pr_name = models.CharField(max_length=30)


#作者表
class Authors(models.Model):
    au_id = models.AutoField(primary_key=True)
    au_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

#类型表
class BookType(models.Model):
    bt_id = models.AutoField(primary_key=True)
    bt_name = models.CharField(max_length=30)

#图书表
class Books(models.Model):
    bk_id = models.AutoField(primary_key=True)
    bk_name = models.CharField(max_length=30)
    price = models.FloatField(max_length=30)
    intro = models.CharField(max_length=300)
    img = models.CharField(max_length=100)
    bt_type = models.ForeignKey(BookType) #和类型的关系
    presses = models.ForeignKey(Press) #和出版社的关系
    authors = models.ForeignKey(Authors) #和作者的关系

#借书人表
class Borrow_persons(models.Model):
    bp_id = models.AutoField(primary_key=True)
    bp_name = models.CharField(max_length=30)
    bp_books = models.ManyToManyField(Books) #和图书的关系


#借书表
class Borrow_books(models.Model):
    bb_id = models.AutoField(primary_key=True)
    bb_bdate = models.DateField(auto_now=True) #借书日期
    bb_rdate = models.DateField(auto_now=True) #还书日期
    bk_name = models.ForeignKey(Books) #和图书的关系
    bp_name = models.ForeignKey(Borrow_persons) #和借书人的关系