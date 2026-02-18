from django.db.models.signals import post_save
from django.dispatch import receiver

# This effectively stops Django from saving Admin logs
@receiver(post_save)
def disable_logs(sender, **kwargs):
    if sender.__name__ == 'LogEntry':
        pass # Do nothing, effectively blocking the log