from xmlrpc.client import DateTime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, TextField, ForeignKey


class VotDigital(models.Model):
    proposal = models.TextField(help_text="The proposal text")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Proposal by {}: {}".format(self.owner, self.proposal[:100])

    def vote_results(self):
        results = {}
        for i in Vote.VOTE_OPTIONS:
            results[i[1]] = self.vote_set.filter(vote_value=i[0]).count()
        return results

class Vote(models.Model):
    VOTE_NO = 0
    VOTE_YES = 1
    VOTE_ABS = 2

    VOTE_OPTIONS = [[VOTE_NO, "no"],[VOTE_YES, "yes"], [VOTE_ABS, "abstain"]]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    topic = models.ForeignKey(VotDigital, on_delete=models.CASCADE)
    #, related_name=votes
    vote_value = models.IntegerField(choices = VOTE_OPTIONS)

    def __str__(self):
        return "{} voted {} for #{}".format(self.owner, self.get_vote_value_display(), self.topic.id)

    def get_vote_value_display(self):
        pass