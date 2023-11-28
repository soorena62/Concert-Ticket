from django.db import models

# Create your models here:


class Concert(models.Model):
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    length = models.IntegerField()
    poster = models.ImageField(upload_to="ConcertImages/")

    def __str__(self):
        return self.singer
     

class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
    

class Time(models.Model):
    start = models.DateTimeField()
    seats = models.IntegerField()
    concert = models.ForeignKey(to=Concert, on_delete=models.PROTECT)
    location = models.ForeignKey(to=Location, on_delete=models.PROTECT)

    Start = 1
    Selling = 2
    Cancel = 3
    End = 4
    status_choices = (
        ("Start", "Ticket sales have started"),
        ('Selling', "Ticket selling"),
        ('Cancel', "This screening has been cancelled"),
         ('End', "Ticket sales have ended")
    )
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(Time.start, Concert.name, Location.name)
    

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="ProfileImages/", null=True)

    Man = 1
    Woman = 2
    status_choices = (("Man", "Male"),("Woman", "Female"))
    gender = models.IntegerField(choices=status_choices)

    def __str__(self):
        return "FullName: {} {}".format(Profile.first_name, Profile.last_name)
    

class Ticket(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=models.PROTECT)
    time = models.ForeignKey("Time", on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    ticket_images = models.ImageField(upload_to="TicketImages/")

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(Time.__str__())
