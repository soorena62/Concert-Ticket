from django.db import models
from django.contrib.auth.models import User
# Create your models here:



class Profile(models.Model):
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", verbose_name="کاربری")
    profile_image = models.ImageField(upload_to="ProfileImages/", null=True, verbose_name="عکس")
    
    Man = 1
    Woman = 2
    status_choices = ((Man, "مرد"),(Woman, "زن"))
    gender = models.IntegerField(choices=status_choices, verbose_name="جنسیت")
    credit = models.IntegerField(verbose_name='اعتبار', default=0)

    
