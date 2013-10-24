from django.db import models

from datetime import datetime

class Idea(models.Model):
    title = models.CharField(max_length=2048)
    description = models.TextField()

    owner = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

    @models.permalink
    def get_absolute_url(self):
        return ('idea-detail', (), {'idea_id': self.pk})

    @models.permalink
    def get_voteup_url(self):
        return ('idea-vote-up', (), {'idea_id': self.pk})

    @models.permalink
    def get_votedown_url(self):
        return ('idea-vote-down', (), {'idea_id': self.pk})

    @models.permalink
    def get_comment_url(self):
        return ('idea-comment', (), {'idea_id': self.pk})

class Vote(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    value = models.IntegerField(choices=(
        (-1, 'Down'),
        (1, 'Up'),
    ))

    class Meta:
        unique_together = (
            ('user', 'idea'),
        )

class Comment(models.Model):
    idea = models.ForeignKey('Idea')
    user = models.ForeignKey('auth.User')

    created = models.DateTimeField(default=datetime.now)

    comment = models.TextField()

    class Meta:
        ordering = ('created',)
