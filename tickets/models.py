from django.db import models
from jalali_date import datetime2jalali, date2jalali
# Create your models here:


class Concert(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="نام کنسرت")
    singer = models.CharField(max_length=100, verbose_name="خواننده")
    length = models.IntegerField()
    poster = models.ImageField(upload_to="ConcertImages/", verbose_name="پوستر")

    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"

    def __str__(self):
        return self.singer
     

class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name="نام محل")
    address = models.CharField(max_length=300, verbose_name="آدرس")
    phone = models.CharField(max_length=13, verbose_name="تلفن")
    capacity = models.IntegerField(verbose_name="ظرفیت")
    
    class Meta:
        verbose_name = "محل برگزاری"
        verbose_name_plural = "محل برگزاری"

    def __str__(self):
        return self.name
    

class Time(models.Model):
    start = models.DateTimeField(verbose_name="تاریخ برگزاری")
    seats = models.IntegerField(verbose_name="تعداد صندلی ها")
    concert = models.ForeignKey(to=Concert, on_delete=models.PROTECT, verbose_name="کنسرت")
    location = models.ForeignKey(to=Location, on_delete=models.PROTECT, verbose_name="محل برگزاری")

    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس"

    Start = 1
    Selling = 2
    Cancel = 3
    End = 4
    status_choices = (
        (Start, "فروش بلیط شروع شده است"),
        (Selling, "در حال فروش بلیط"),
        (Cancel, "این سانس لغو شده است"),
         (End, "فروش بلیط پایان یافته است")
    )
    status = models.IntegerField(choices=status_choices, verbose_name="وضعیت")

    def __str__(self):
        return "نام: {} /  مکان: {} / زمان: {}".format(self.concert.name, self.location.name, self.start)
    
    def get_jalali_date(self):
        return datetime2jalali(self.start)


class Profile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="نام")
    last_name = models.CharField(max_length=50, verbose_name="نام خانوادگی")
    profile_image = models.ImageField(upload_to="ProfileImages/", null=True, verbose_name="عکس")

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    Man = 1
    Woman = 2
    status_choices = (("Man", "مرد"),("Woman", "زن"))
    gender = models.IntegerField(choices=status_choices, verbose_name="جنسیت")

    def __str__(self):
        return "FullName: {} {}".format(Profile.first_name, Profile.last_name)
    

class Ticket(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=models.PROTECT, verbose_name="کاربر")
    time = models.ForeignKey("Time", on_delete=models.PROTECT, verbose_name="سانس")
    name = models.CharField(max_length=100, verbose_name="عنوان")
    price = models.IntegerField(verbose_name="مبلغ")
    ticket_images = models.ImageField(upload_to="TicketImages/", verbose_name="عکس")

    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط"

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(Time.__str__())
