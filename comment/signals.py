from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from comment.models import Comment
from catalog.models import HotelCatalog


@receiver(post_save, sender=Comment)
def post_save_comment(sender, instance, created, **kwargs):
    if created:
        print('Comment saved. Calculate new rating')
        recalculate_info_rating(instance_info=instance.info_hotelcatalog)


@receiver(post_delete, sender=Comment)
def post_delete_comment(sender, instance, **kwargs):
    print('Comment deleted. Calculate new rating')
    recalculate_info_rating(instance_info=instance.info_hotelcatalog)


def recalculate_info_rating(instance_info: HotelCatalog):
    comments = instance_info.comments.all()
    total_rating = sum(comment.rating for comment in comments)
    instance_info.rating = total_rating / len(comments) if comments else 0
    instance_info.save()
