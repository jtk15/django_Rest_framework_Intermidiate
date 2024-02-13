from django.db import models



class Base(models.Model):
    
    criation = models.DateTimeField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        
        abstract = True

class Course(Base):
    
    title = models.CharField('Titulo', max_length=100)
    url = models.CharField(max_length=200)
    
    class Meta:
        
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        
        return self.title
    


class Assessment(Base):
     
    course = models.ForeignKey(Course, related_name='assessments', on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
    
    class Meta:
    
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'course']
    
    def __str__(self):
        
        return 'Avaliação'
    