import slugify
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Book name",
        help_text="max length 200",
        unique_for_date='published_date',
        null=True,
        blank=True,
    )
    image_color = ColorField(format="hexa")
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    changed_date = models.DateTimeField(auto_now=True, editable=False)
    slug = models.SlugField(null=True, editable=False)
    content = RichTextField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, limit_choices_to={
        'is_superuser': False,
        'is_staff': True,
    },
                              related_name='books')
    authors = models.ManyToManyField('Author')

    def save(self, *a, **kw):
        self.slug = slugify.slugify(f"{self.title} - {self.published_date}")
        return super().save(*a, **kw)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors')
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


# models.ForeignKey
# models.OneToOneField
# models.ManyToManyField


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    boss = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    slaves = models.ManyToManyField('self', null=True, blank=True)
    changed_count = models.IntegerField(editable=False, default=0)

    # slaves_count = models.IntegerField(editable=False)
    #
    # def save(self, *a, **kw):  # commit to DB
    #     self.slaves_count = self.slaves.count()
    #     return super().save(*a, **kw)

    @property
    def slaves_count(self):
        return self.slaves.count()

    @property
    def boss_name(self):
        if self.boss:
            return f'{self.boss.user.first_name} {self.boss.user.last_name}'
        return ''

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-user',)
        default_related_name = "employer_set"
