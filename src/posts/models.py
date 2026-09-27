from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Текст')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='URL-идентификатор')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    photo = models.ImageField(upload_to='posts/', verbose_name='Постер', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return self.photo.url
