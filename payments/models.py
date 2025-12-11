from django.db import models
from django.conf import settings

class Payment(models.Model):
    PAYMENT_TYPES = [
        ('Tuition','Tuition'),
        ('Exam','Exam'),
        ('Transport','Transport'),
        ('Hostel','Hostel'),
        ('Other','Other'),
    ]
    STATUS = [('paid','Paid'),('pending','Pending'),('failed','Failed')]

    student = models.ForeignKey('student.Student', on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=32, choices=PAYMENT_TYPES, default='Tuition')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=64, blank=True)
    reference_id = models.CharField(max_length=128, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    note = models.TextField(blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-payment_date']

    def __str__(self):
        return f"{self.student} - {self.amount} - {self.payment_type}"
