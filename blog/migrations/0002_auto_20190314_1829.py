# Generated by Django 2.1.7 on 2019-03-14 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categorie',
            field=models.CharField(choices=[('Annonce', 'Annonce'), ('Agenda', 'Agenda'), ('Rencontre', 'Rencontre'), ('Chantier', 'Chantier participatif'), ('Jardinage', 'Jardinage'), ('Recette', 'Recette'), ('Histoire', 'Histoire'), ('Bricolage', 'Bricolage'), ('Culture', 'Culture'), ('Bon_plan', 'Bon plan'), ('Point', 'Point de vue'), ('Autre', 'Autre')], default='Annonce', max_length=30, verbose_name='categorie'),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='auteur_comm',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='contenu',
            field=tinymce.models.HTMLField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='auteur',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
