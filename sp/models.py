from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.core.validators import RegexValidator


class Call(models.Model):
    user_id = models.ForeignKey(User, verbose_name='id пользователя')
    call_types = (
        (True, 'Предложение'),
        (False, 'Поиск'),
    )
    type = models.BooleanField(choices=call_types, default=True, verbose_name='Тип')
    city = models.CharField(max_length=30, verbose_name='Город')
    name = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    card = models.ImageField(upload_to="sp/cards", blank=True, verbose_name='Изображение')
    tags = TaggableManager(blank=True, help_text='Список ключевых слов, взятых в кавычки, через запятую',
                           verbose_name='Ключевые слова')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='id пользователя')
    name = models.CharField(max_length=30, verbose_name='Имя', blank=True,
                            validators=[RegexValidator(regex='^[a-zA-ZА-Яа-я]+$',
                                                       message='Введите правильное имя или оставьте поле пустым')])
    surname = models.CharField(max_length=30, verbose_name='Фамилия', blank=True)
    city = models.CharField(max_length=30, verbose_name='Город', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True, help_text='Формат даты: гггг-мм-дд')
    education = models.CharField(max_length=70, verbose_name='Образование', blank=True)
    genders = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    gender = models.CharField(choices=genders, verbose_name='Пол', max_length=30, blank=True)
    offers = models.TextField(verbose_name='Предложения', blank=True)
    search = models.TextField(verbose_name='Поиск', blank=True)
    e_mail = models.CharField(max_length=30, verbose_name='E-mail',
                              validators=[RegexValidator(regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
                                                         message='Введите правильный e-mail')])
    contacts = models.TextField(verbose_name='Другие контакты', blank=True)

    def __str__(self):
        return str(self.user_id)
