from django import forms
from .models import Article, Commentaire, Projet, CommentaireProjet
from django.utils.text import slugify
import itertools
from django.utils.timezone import now
from django.utils.formats import localize
from tinymce.widgets import TinyMCE


class ArticleForm(forms.ModelForm):
    #contenu = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    contenu = TinyMCE(attrs={'cols': 80, 'rows': 20})
    estPublic = forms.ChoiceField(choices=((1, "Article public"), (0, "Article Permacat")), label='', required=True)

    class Meta:
        model = Article
        fields = ['categorie', 'titre', 'contenu', 'estPublic']

    def save(self, userProfile):
        instance = super(ArticleForm, self).save(commit=False)

        max_length = Article._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.titre)[:max_length]

        for x in itertools.count(1):
            if not Article.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.date = localize(now, use_l10n=True)
        instance.auteur = userProfile
        if not userProfile.is_permacat:
            instance.estPublic = True

        instance.save()

        return instance


    def __init__(self, request, message=None, *args, **kwargs):
        super(ArticleForm, self).__init__(request, *args, **kwargs)
        self.fields['contenu'].strip = False

class ArticleChangeForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['categorie', 'titre', 'contenu', 'estPublic', ]

    def __init__(self, *args, **kwargs):
        super(ArticleChangeForm, self).__init__(*args, **kwargs)
        self.fields['contenu'].strip = False

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        exclude = ['article','auteur_comm']

        widgets = {
                'commentaire': forms.Textarea(attrs={'rows': 1}),
            }

    def __init__(self, request, *args, **kwargs):
        super(CommentForm, self).__init__(request, *args, **kwargs)
        self.fields['commentaire'].strip = False

class ProjetForm(forms.ModelForm):
    #contenu = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 10}))
    contenu = TinyMCE(attrs={'cols': 80, 'rows': 20})
    estPublic = forms.ChoiceField(choices=((1, "Projet public"), (0, "Projet Permacat")), label='', required=True)

    class Meta:
        model = Projet
        fields = ['categorie','coresponsable', 'titre', 'contenu', 'estPublic', 'lien_document', 'fichier_projet', 'lien_vote',]

    def __init__(self, request, *args, **kwargs):
        super(ProjetForm, self).__init__(request, *args, **kwargs)
        self.fields['contenu'].strip = False

    def save(self, userProfile):
        instance = super(ProjetForm, self).save(commit=False)

        max_length = Projet._meta.get_field('slug').max_length
        instance.slug = orig = slugify(instance.titre)[:max_length]

        for x in itertools.count(1):
            if not Projet.objects.filter(slug=instance.slug).exists():
                break

            # Truncate the original slug dynamically. Minus 1 for the hyphen.
            instance.slug = "%s-%d" % (orig[:max_length - len(str(x)) - 1], x)

        instance.date = localize(now, use_l10n=True)
        instance.auteur = userProfile

        if not userProfile.is_permacat:
            instance.estPublic = True

        instance.save()

        return instance


class ProjetChangeForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['categorie', 'coresponsable', 'titre', 'contenu', 'estPublic', 'lien_document','fichier_projet', 'lien_vote']

    def __init__(self, *args, **kwargs):
        super(ProjetChangeForm, self).__init__(*args, **kwargs)
        self.fields['contenu'].strip = False

class CommentProjetForm(forms.ModelForm):
    class Meta:
        model = CommentaireProjet
        exclude = ['projet','auteur_comm']

        widgets = {
                'commentaire': forms.Textarea(attrs={'rows': 1}),
            }

    def __init__(self, request, *args, **kwargs):
         super(CommentProjetForm, self).__init__(request, *args, **kwargs)
         self.fields['commentaire'].strip = False