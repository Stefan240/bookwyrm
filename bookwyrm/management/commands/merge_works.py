""" PROCEED WITH CAUTION: uses deduplication fields to permanently
merge work data objects """
from bookwyrm import models
from bookwyrm.management.merge_command import MergeCommand


class Command(MergeCommand):
    """merges two works by ID"""

    help = "merges specified works into one"

    MODEL = models.Work
