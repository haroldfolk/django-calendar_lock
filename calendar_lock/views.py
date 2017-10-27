
# Create your views here.
import datetime

from django.shortcuts import get_object_or_404, render

from calendar_lock.models import Date_lock

def index(request):
    if request.method == 'POST':
        date_to_lock = request.POST.get('date')
        reason_to_lock=request.POST.get('reason')
        y = date_to_lock[0:4]
        m = date_to_lock[5:7]
        d = date_to_lock[8:10]
        date_formated = datetime.datetime(int(y), int(m), int(d), 0, 0, 0)
        lock_date(date_formated,reason_to_lock)
    dates_locked=Date_lock.objects.all()

    return render(request, 'calendar_lock/index.html',{'dates_locked':dates_locked})

def lock_date(date,reason):
    date_locking=Date_lock()
    date_locking.date_locked=date
    date_locking.reason_locked=reason
    date_locking.save()

def unlock_date(date):
    date_unlocking=get_object_or_404(Date_lock,date_locked=date)
    date_unlocking.delete()

def change_reason_locked(date,reason):
    date_changing = get_object_or_404(Date_lock, date_locked=date)
    date_changing.reason_locked=reason
    date_changing.save()

def return_reason_lock_date(date):
    date_consulting=get_object_or_404(Date_lock,date_locked=date)
    return date_consulting.reason_locked