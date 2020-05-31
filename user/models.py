from django.db import models

# Create your models here.
class User(models.Model):
  email = models.EmailField(verbose_name='Email')
  password = models.CharField(max_length=128, verbose_name='Password')
  level = models.CharField(max_length=8, verbose_name='User level',
    choices={
      ('admin', 'admin'),
      ('user', 'user')
    })
  register_date = models.DateTimeField(auto_now_add=True, verbose_name='Register Date')

  def __str__(self):
    return self.email

  class Meta:
    db_table = 'Jamie\'s shop_user'
    verbose_name = 'User'
    verbose_name_plural = 'User'