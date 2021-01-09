from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Game(models.Model):
    chinese_name = models.CharField(max_length=50)
    english_name = models.CharField(max_length=50, null=True, blank=True)
    japanese_name = models.CharField(max_length=50, null=True, blank=True)

    release_date = models.DateField(blank=True)
    type = models.ManyToManyField('GameType')

    def get_type(self):
        return '/'.join([i.types for i in self.type.all()])

    platform = models.ManyToManyField('Platform')

    def get_platform(self):
        return '/'.join([i.platforms for i in self.platform.all()])

    serie = models.ForeignKey('Series', on_delete=models.SET_NULL, null=True)

    language = models.ManyToManyField('Language')

    def get_language(self):
        return '/'.join([i.languages for i in self.language.all()])

    company = models.ManyToManyField('Company')

    def get_company(self):
        return '/'.join([i.companies for i in self.company.all()])

    demo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.chinese_name

    target = models.ManyToManyField('Target')

    def get_target(self):
        return '/'.join([i.targets for i in self.target.all()])


class GameType(models.Model):
    gameType_choice = (
        ('action games', 'Action games'),
        ('action-adventure games', 'Action-adventure games'),
        ('adventure games', 'Adventure games'),
        ('role-playing games', 'Role-playing games'),
        ('simulation games', 'Simulation games'),
        ('strategy games', 'Strategy games'),
        ('sports games', 'Sports games'),
        ('puzzle games', 'Puzzle games'),
        ('idle games', 'Idle games'),
    )
    types = models.CharField(max_length=30, choices=gameType_choice)

    def __str__(self):
        return self.types


class Platform(models.Model):
    platform_choice = (
        ('iOS', 'iOS'),
        ('android', 'Android'),
        ('PS4', 'PS4'),
        ('switch', 'Switch'),
        ('xbox_one_X', 'XBOX ONE X'),
    )
    platforms = models.CharField(max_length=15)

    def __str__(self):
        return self.platforms


class Series(models.Model):
    series = models.CharField(max_length=40)

    def __str__(self):
        return self.series


class Language(models.Model):
    language_choice = (
        ('CHINESE', 'CHINESE'),
        ('SPANISH', 'SPANISH'),
        ('ENGLISH', 'ENGLISH'),
        ('HINDI', 'HINDI'),
        ('ARABIC', 'ARABIC'),
        ('PORTUGUESE', 'PORTUGUESE'),
        ('BENGALI', 'BENGALI'),
        ('RUSSIAN', 'RUSSIAN'),
        ('JAPANESE', 'JAPANESE'),
        ('LAHNDA', 'LAHNDA'),
        ('JAVANESE', 'JAVANESE'),
        ('GERMAN', 'GERMAN'),
        ('KOREAN', 'KOREAN'),
        ('FRENCH', 'FRENCH'),
        ('TELUGU', 'TELUGU'),
        ('TURKISH', 'TURKISH'),
        ('TAMIL', 'TAMIL'),
        ('VIETNAMESE', 'VIETNAMESE'),
        ('URDU', 'URDU'),
    )
    languages = models.CharField(max_length=20, choices=language_choice)

    def __str__(self):
        return self.languages


class Company(models.Model):
    companies = models.CharField(max_length=30)

    def __str__(self):
        return self.companies


class Target(models.Model):
    targets = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.targets


# Room Model------------------------------


class Room(models.Model):
    language_choice = (
        ('English', 'English'),
        ('Japanese', 'Japanese'),
        ('Chinese', 'Chinese'),
    )
    player_choice = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    game = models.CharField(max_length=50, null=True)
    host = models.CharField(max_length=40, blank=True, default='host')
    guest_id = models.CharField(max_length=40, blank=True, default='guest')
    target = models.ForeignKey(Target, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=60, null=True, blank=True)
    requirement = models.CharField(max_length=100, null=True, blank=True)
    language = models.CharField(max_length=20, choices=language_choice)
    player = models.CharField(max_length=2, choices=player_choice, blank=True, default='4')
    room_id = models.CharField(max_length=30, null=True)
    game_password = models.CharField(max_length=20, null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, null=True)
    version = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


