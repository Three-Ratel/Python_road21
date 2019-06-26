from django.db import models


class Person(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_column='username', help_text='xxx')
    age = models.IntegerField(unique=True)
    birth = models.DateTimeField(auto_now_add=True, db_index=True)
    time = models.DateTimeField(auto_now=True)
    gender = models.BooleanField('性别', choices=((0, 'female'), (1, 'male'),))
    addr = models.CharField(max_length=50, null=True, blank=True,
                            verbose_name='地址', editable=True)

    def __str__(self):
        return '{}{}'.format(self.name, self.age)

    class Meta:
        db_table = 'person'
        verbose_name = '个人信息'
        verbose_name_plural = '所有信息'
        index_together = [('name', 'age')]
        unique_together = [('birth', 'age')]


class Publisher(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return '{}'.format(self.name)


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pub = models.ForeignKey('Publisher', related_query_name='books')

    def __str__(self):
        return '{}'.format(self.title)


class MyCharField(models.Field):

    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharField, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        return 'char(%s)' % self.max_length


class Test(models.Model):
    # name = MyCharField(max_length=20)
    gender_list = (('0', 'female'), (1, 'male'),)
    gender = models.CharField(max_length=1, choices=gender_list)
    models.ManyToManyField

