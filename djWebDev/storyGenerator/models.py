from django.db import models

class Story(models.Model):
    protagonist = models.CharField(max_length=30)
    antagonist = models.CharField(max_length=30)
    setting = models.CharField(max_length=30)
    SETTING_CHOICES = (
        ('spc', 'SPACE'),
        ('wstrn', 'WESTERN'),
        ('ar', 'ANCIENT ROME'),
        ('dysf', 'DYSTOPIA FUTURE')
    )
    plot = models.CharField(max_length=30)
    conflict = models.CharField(max_length=30)
    genre = models.CharField(max_length=60)

'''
class Genre(models.Model):
    """Story genre"""
    name = models.CharField(max_length=200, help_text='Enter a genre for your story (e.g. Fantasy)')

    def __str__(self):
        return self.name


class BlankStory(models.Model):
    """Model to hold information for a story template"""
    title = models.CharField(max_length=200,help_text='Enter the title of the story', primary_key=True)

    contents = models.TextField(help_text='Enter your story, using <word_type> to indicate where we should make openings in your template')

    adjectiveCount = models.IntegerField()
    nounCount = models.IntegerField()
    adverbCount = models.IntegerField()
    plurNounCount = models.IntegerField()
    verbCount = models.IntegerField()

    genre = models.ManyToManyField(Genre,help_text='Select a genre for the story')

    #completedStories = model.ManyToManyField('WordSet')


class WordSet(models.Model):
    adverbs = models.TextField()
    nouns = models.TextField()
    plurNouns = models.TextField()
    verbs = models.TextField()
    adjectives = models.TextField()

    story = models.ForeignKey('BlankStory',on_delete=models.SET_NULL,null=True)
'''
