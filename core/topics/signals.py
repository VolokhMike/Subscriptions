from django.db.models.signals import post_save, post_delete, m2m_changed
from django.dispatch import receiver, Signal
from django.core.cache import cache
from .models import Topic, TopicActivity


topic_changed = Signal()


@receiver(m2m_changed, sender=Topic.subscribers.through)
def subscribers_changed(sender, instance, action, pk_set, **kwargs):
    if action in ('post_add', 'post_remove', 'post_clear'):
        for user_id in pk_set:
            cache.delete(f"user:{user_id}:topics")


@receiver(post_save, sender=Topic)
def topic_saved(sender, instance, created, **kwargs):
    if created:
        TopicActivity.objects.create(
            topic=instance,
            action='created'
        )
        topic_changed.send(
            sender=sender,
            topic_id=instance.id,
            action='created'
        )


@receiver(post_delete, sender=Topic)
def topic_deleted(sender, instance, **kwargs):
    TopicActivity.objects.create(
        topic=instance,
        action='deleted'
    )
    topic_changed.send(
        sender=sender,
        topic_id=instance.id,
        action='deleted'
    )


def handle_topic_changed(sender, topic_id, action, **kwargs):
    print(f"Topic {topic_id} changed: {action}")
    cache.clear()
