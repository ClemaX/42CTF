from collections import defaultdict
from django.core.management.base import BaseCommand, CommandError
from accounts import models as acc_models
from ctfs import models as ex_models

class Command(BaseCommand):
    help = 'Recomputes the score and ranking caches from the solutions'

    def handle(self, *args, **options):
        all_sols = ex_models.CTF_flags.objects.select_related().filter(ctf__event=None)
        scores = defaultdict(int)
        for sol in all_sols:
            scores[sol.user] += sol.ctf.points
        li = [(s, u) for (u, s) in scores.items()]

        li2 = []
        old_rank = None
        old_score = None
        rank = 0
        for (s, u) in li:
            rank += 1
            if s == old_score:
                li2.append((u, s, old_rank))
            else:
                old_score = s
                old_rank = rank
                li2.append((u, s, rank))

        for (u, s, r) in li2:
            u.userprofileinfo.score = s
            u.userprofileinfo.save()
