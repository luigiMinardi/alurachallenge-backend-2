from django.db import models

class Income(models.Model):
    description = models.CharField(
        max_length=500,
        help_text="Put the description of your income"
    )
    value = models.DecimalField(
        decimal_places=2,
        max_digits=20
    )
    date = models.DateField(
        auto_now_add=True
    )
    
    def __str__(self):
        return self.value