from django.db import models
from django.contrib import admin
class Advertisements(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text="отметье, если торг уместен")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Advertisement={self.id}, title={self.title}, price={self.price}"

    @admin.display(description='дата создания')
    def create_dated(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">'
                'сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')


    @admin.display(description='дата обновления')
    def update_dated(self):
        from django.utils import timezone
        from django.utils.html import format_html
        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: green; font-weight: bold">'
                'сегодня в {}</span>', update_time
    )
        return self.update_at.strftime('%d.%m.%Y в %H:%M:%S')



class Meta:
    db_table = "advertisements"

# Create your models here.
