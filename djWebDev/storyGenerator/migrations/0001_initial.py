# Generated by Django 3.1.2 on 2020-11-02 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlankStory',
            fields=[
                ('title', models.CharField(help_text='Enter the title of the story', max_length=200, primary_key=True, serialize=False)),
                ('contents', models.TextField(help_text='Enter your story, using <word_type> to indicate where we should make openings in your template')),
                ('adjectiveCount', models.IntegerField()),
                ('nounCount', models.IntegerField()),
                ('adverbCount', models.IntegerField()),
                ('plurNounCount', models.IntegerField()),
                ('verbCount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a genre for your story (e.g. Fantasy)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WordSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adverbs', models.TextField()),
                ('nouns', models.TextField()),
                ('plurNouns', models.TextField()),
                ('verbs', models.TextField()),
                ('adjectives', models.TextField()),
                ('story', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='storyGenerator.blankstory')),
            ],
        ),
        migrations.AddField(
            model_name='blankstory',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for the story', to='storyGenerator.Genre'),
        ),
    ]