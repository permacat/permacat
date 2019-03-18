from django.db import models
from bourseLibre.models import Profil
from django.urls import reverse
#from django.conf import settings
from tinymce.models import HTMLField

# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=64)
#     date = models.DateTimeField()
#     author = models.ForeignKey(User)
#     body = models.TextField()
#  
#     def __str__(self):
#         return "%s (%s)" % (self.title, self.author.name)
#     
    
class Article(models.Model):
    categorie = models.CharField(max_length=30,         
        choices=(('Annonce','Annonce'), ('Agenda','Agenda'), ('Rencontre','Rencontre'), ('Chantier','Chantier participatif'), ('Jardinage','Jardinage'), ('Recette', 'Recette'), ('Histoire', 'Histoire'), ('Bricolage','Bricolage'), ('Culture','Culture'), ('Bon_plan', 'Bon plan'), ('Point', 'Point de vue'),  ('Autre','Autre'),),
        default='Annonce', verbose_name="categorie")
    titre = models.CharField(max_length=100)
    auteur = models.ForeignKey(Profil, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100)
    contenu = HTMLField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
    
    class Meta:
        ordering = ('date', )
        
    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('blog:lireArticle', kwargs={'slug':self.slug})
#     @models.permalink
#     def get_url(self):
#         return ('blog_post_detail', (), 
#                 {
#                     'slug' :self.slug,
#                 })

class Commentaire(models.Model):
    auteur_comm = models.ForeignKey(Profil, on_delete=models.CASCADE)
    titre = models.CharField(max_length=42)
    commentaire = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.titre
