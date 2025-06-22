# views.py
from django.shortcuts import render,HttpResponse
from login.models import Seat
for s in Seat.objects.all():
    print(s.seatid, s.status)

def htm(request):
    return render(request, "login/main.html")  

def booking(request):
    seats_qs = Seat.objects.all()
    seats = {seat.seatid.lower(): seat for seat in seats_qs}  
    return render(request, "login/book.html", context={'seats': seats, 'seat2': seats_qs})
def seat_booking(request):
    seats = Seat.objects.all()

    if request.method == 'POST':
        seat_no = request.POST.get('seatno', '')

        try:
            seat = Seat.objects.get(seatid=seat_no)


            if seat.status == 'empty':
               seat.status = 'reserved'
               seat.status = 'reserved'
               seat.save()
               seat.refresh_from_db()
               print(f"[DEBUG] Seat {seat.seatid} saved with status: {seat.status}")
               return HttpResponse(f'Seat {seat_no} successfully reserved.')
            else:
                return HttpResponse(f'Seat {seat_no} is already booked.')

        except Seat.DoesNotExist:
            return HttpResponse(f'Seat {seat_no} does not exist.')

    return render(request, 'login/booking.html', context={'seats': seats})
def menu(request):
    return render(request, 'login/menu.html')
def gallery(request):
    return render(request, 'login/gallery.html')