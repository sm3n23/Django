import telepot
from django.core.mail import send_mail
from django.db import models

# Create your models here.
import os
from django.db import models

class Dht(models.Model):
  temp = models.FloatField(null=True)
  hum = models.FloatField(null=True)
  dt = models.DateTimeField(auto_now_add=True,null=True)
  def __str__(self):
    return str(self.temp)

  def save(self, *args, **kwargs):

       if self.temp > 40:
         token = '5906116835:AAFXkps_D43lRvsnxinWNl6b6iaKad7KuSE'
         rece_id = 1348341201
         bot = telepot.Bot(token)
         bot.sendMessage(rece_id, 'température dépasse la normale,' + str(self.temp))
         print(bot.sendMessage(rece_id, 'OK.'))

         send_mail(
           'température dépasse la normale,' + str(self.temp),
           'anomalie dans la machine',
           'ismail.elattar1@ump.ac.ma',
           ['ismailelattar777@gmail.com'],
           fail_silently=False,

         )
       return super().save(*args, **kwargs)

