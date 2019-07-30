from django.db import models

class Actor(models.Model):
    Gender = (
        ('M','Male'),
        ('F','Female'),
    )
    actor = models.CharField(max_length=264,unique=True)   
    sex = models.CharField(max_length=1,choices=Gender)
    DOB = models.DateField()    
    Bio = models.TextField()
    actor_image = models.ImageField(upload_to='media',blank=True)
    def __str__(self):
        return '{}\t{}\t{}'.format(self.actor.actor,self.DOB,self.sex)

    def __str__(self):
        return self.actor

class Movie(models.Model):
    Gener = (
        ('Action','Action'),
        ('Adventure' , 'Adventure'),
        ('Animation' , 'Animation'),
        ('Comedy' , 'Comedy'),
        ('Crime' , 'Crime'),
        ('Drama' , 'Drama'),
        ('Family' , 'Family'),
        ('Fantacy' , 'Fantasy'),
        ('Horror' , 'Horror'),
        ('Mystrey' , 'Mystrey'),
        ('Thriller' , 'Thriller'),
        ('Sci-fi' , 'Sci-fi'),
        ('Romance' , 'Romance'),
    )
    Status = (
        ('RecentlyAdded' ,'Recently Added'),
        ('TopRated', 'Top Rated') ,
        ('MostWatched','Most Watched'),
    )
    language = (
        ('ENGLISH','English'),
        ('TELUGU','Telugu'),
        ('HINDHI','Hindhi'),
        ('TAMIL','Tamil'),
    )
    movie = models.CharField(max_length=264,unique=True)
    movie_actor = models.ManyToManyField(Actor)
    lang = models.CharField(max_length=10,choices=language)
    gener = models.CharField(max_length=10,choices=Gener)
    status = models.CharField(max_length=20,choices=Status)
    release_date = models.DateField()
    plot = models.TextField(max_length=1024)
    movie_image = models.ImageField(upload_to='media')
    
    def get_actor_values(self):
        ret = ''
        print(self.movie_actor.all())
        
        for actors in self.movie_actor.all():
            ret = ret + actors.actor + ','
        return ret[:-1]         

class Tvshow(models.Model):
    Gener = (
        ('Action','Action'),
        ('Adventure' , 'Adventure'),
        ('Animation' , 'Animation'),
        ('Comedy' , 'Comedy'),
        ('Crime' , 'Crime'),
        ('Drama' , 'Drama'),
        ('Family' , 'Family'),
        ('Fantacy' , 'Fantasy'),
        ('Horror' , 'Horror'),
        ('Mystrey' , 'Mystrey'),
        ('Thriller' , 'Thriller'),
        ('Sci-fi' , 'Sci-fi'),
        ('Romance' , 'Romance'),
    )
    Status = (
        ('RecentlyAdded' ,'Recently Added'),
        ('TopRated', 'Top Rated') ,
        ('MostWatched','Most Watched'),
    )
    language = (
        ('ENGLISH','English'),
    )
    tvshow = models.CharField(max_length=264,unique=True)
    tv_actor = models.ManyToManyField(Actor)
    lang = models.CharField(max_length=10,choices=language)
    gener = models.CharField(max_length=10,choices=Gener)
    status = models.CharField(max_length=20,choices=Status)
    release_date = models.DateField()
    plot = models.TextField(max_length=1024)
    tvshow_image = models.ImageField(upload_to='media')
    
    def get_actor_values(self):
        ret = ''
        print(self.tv_actor.all())
        
        for actors in self.tv_actor.all():
            ret = ret + actors.actor + ','
        return ret[:-1]           

 






