# Python
from typing import Any
import psycopg2
# Django
from django.db.models.signals import (
    post_delete,
    post_save
)
from django.dispatch import receiver

# Local
from mesages.models import Message


@receiver(post_save, sender=Message)
def save_message(sender, instance, **kwargs):
    connection = psycopg2.connect(
        dbname='itstep2',
        user='postgres',
        password='root',
        host='localhost',
        port='5432'
    )
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS itstep2 (id SERIAL PRIMARY KEY, text TEXT)')
    cursor.execute(
        'INSERT INTO itstep2 (text) VALUES (%s)', [instance.text])
    connection.commit()
    cursor.close()
    connection.close()
