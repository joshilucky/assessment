# django_signals_examples.py

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading
import time

# A simple model for demonstration
class TestModel(models.Model):
    name = models.CharField(max_length=100)

# Question 1: Are Django signals executed synchronously or asynchronously?
# Answer: Django signals are executed synchronously by default.

@receiver(post_save, sender=TestModel)
def sync_signal_handler(sender, instance, **kwargs):
    print("Signal started - synchronous test")
    time.sleep(5)  # Simulates a delay
    print("Signal completed - synchronous test")

# Question 2: Do Django signals run in the same thread as the caller?
# Answer: Yes, by default, Django signals run in the same thread.

@receiver(post_save, sender=TestModel)
def thread_signal_handler(sender, instance, **kwargs):
    print(f"Signal thread: {threading.current_thread().name}")

# Question 3: Do Django signals run in the same database transaction as the caller?
# Answer: Yes, Django signals run in the same database transaction by default.

@receiver(post_save, sender=TestModel)
def transaction_signal_handler(sender, instance, **kwargs):
    print("Signal started - transaction test")
    raise Exception("Intentional exception to test transaction rollback")
