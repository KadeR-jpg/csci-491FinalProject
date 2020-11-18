from django.db import models


# Create your models here.



class Genre(models.Model):
    """Story genre"""
    name = models.CharField(max_length=200, help_text='Enter a genre for your story (e.g. Fantasy)')

    def __str__(self):
        return self.name


class BlankStory(models.Model):
    """Model to hold information for a story template"""
    title = models.CharField(max_length=200, help_text='Enter the title of the story', primary_key=True)

    contents = models.TextField(
        help_text='Enter your story, using <word_type> to indicate where we should make openings in your template')

    adjectiveCount = models.IntegerField()
    nounCount = models.IntegerField()
    adverbCount = models.IntegerField()
    properNounCount = models.IntegerField()
    pronounCount = models.IntegerField()
    verbCount = models.IntegerField()

    genre = models.ManyToManyField(Genre, help_text='Select a genre for the story')

    # completedStories = model.ManyToManyField('WordSet')


class WordSet(models.Model):
    words = models.TextField(help_text='make sure this is formatted as follows: noun1,noun2|verb1|adverb1,adverb2|pnoun1,pnoun2|pronoun1|adjective1,adjective2')

    story = models.ForeignKey('BlankStory', on_delete=models.SET_NULL, null=True)
