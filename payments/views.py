from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
from .models import Payment
from .forms import PaymentForm
from .utils import render_pdf_from_template
from student.models import Student

def payment_list(request):
    payments = Payment.objects.select_related('student').all()[:200]
    form = PaymentForm()
    return render(request, 'payments/payment_list.html', {'payments': payments, 'form': form})

def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            sid = request.POST.get('student_id')
            try:
                student = Student.objects.get(student_id=sid)
            except Student.DoesNotExist:
                messages.error(request, 'Student not found')
                return redirect('payments_home')
            p = form.save(commit=False)
            p.student = student
            p.created_by = request.user if request.user.is_authenticated else None
            p.save()
            messages.success(request, 'Payment recorded')
            return redirect(reverse('payment_receipt', args=[p.pk]))
    return redirect('payments_home')

def payment_receipt(request, pk):
    p = get_object_or_404(Payment, pk=pk)
    return render_pdf_from_template('payments/receipt.html', {'payment': p})

def dashboard_data(request):
    from django.db.models import Sum, Count
    totals = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    by_status = Payment.objects.values('status').annotate(count=Count('id'))
    recent = list(Payment.objects.select_related('student').order_by('-payment_date')[:10].values('student__name','payment_type','amount','payment_date'))
    return JsonResponse({'total': float(totals), 'by_status': list(by_status), 'recent': recent})
