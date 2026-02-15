from django.db import models


class Suggestion(models.Model):

    CATEGORY_CHOICES = [
        ('general', 'General Suggestion'),
        ('academic', 'Academic Concern'),
        ('facilities', 'Facilities Improvement'),
    ]

    # Optional category selected by student
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        blank=True,
        null=True
    )

    # Raw unstructured feedback (main data)
    content = models.TextField()

    # AI-predicted category (filled later from dashboard logic)
    predicted_category = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    # Timestamp
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Suggestion {self.id} - {self.created_at}"
