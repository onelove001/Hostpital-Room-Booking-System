from django.shortcuts import *
from .models import *
from django.contrib import messages


# Staff Routes
def staff_dashboard_route(request):
    context = {}
    return render(request, "staff/staff_dashboard_route.html", context)


def add_patient(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        user = request.user
        staff_obj = Staff.objects.get(user_profile=user)
        patient = Patient(staff=staff_obj, first_name = first_name, last_name=last_name, username=username, address=address, gender=gender, dob = dob, phone_no=phone)
        patient.save()
        messages.success(request, "Patient Created!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {}
    return render(request, "staff/add_patient.html", context)


def manage_patients(request):
    patients = Patient.objects.all()
    context = {"patients":patients}
    return render(request, "staff/manage_patients.html", context)


def update_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        address = request.POST.get("address")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        phone = request.POST.get("phone")
        patient.first_name = first_name
        patient.last_name = last_name
        patient.username = username
        patient.address = address
        patient.gender = gender
        patient.phone_no = phone
        patient.save()
        messages.success(request, "Patient Updated!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"patient":patient}
    return render(request, "staff/update_patient.html", context)


def delete_patient(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    patient.delete()
    return redirect("app:manage-patients")


def available_rooms(request):
    rooms = Room.objects.filter(status=True)
    context = {"rooms":rooms}
    return render(request, "staff/available_rooms.html", context)


def create_medication(request, patient_id):
    patient = Patient.objects.get(id = patient_id)
    rooms = Room.objects.filter(status=True)
    staff = Staff.objects.get(user_profile=request.user)
    if request.method == "POST":
        drug_prescription = request.POST.get("drug_prescription")
        date_in = request.POST.get("date_in")
        date_out = request.POST.get("date_out")
        book_number = request.POST.get("book_number")
        room = request.POST.get("room")
        room_obj = Room.objects.get(id = room)
        medication_obj = Medication(staff = staff, patient_id=patient, drug_prescription=drug_prescription)
        medication_obj.save()
        room_occu = RoomOccupancies(staff_id=staff, patient_id=patient, book_number=book_number, room_id=room_obj, date_in = date_in, date_out=date_out)
        room_occu.save()
        messages.success(request, 'Success, Please Proceed "Occupants" To Make Payment!')
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"patient":patient, "rooms":rooms}
    return render(request, "staff/create_medication.html", context)


def view_medications(request):
    medications = Medication.objects.all()
    context = {"medications":medications}
    return render(request, "staff/view_medications.html", context)


def update_medication(request, med_id):
    medication = Medication.objects.get(id = med_id)
    if request.method == "POST":
        drug_pre = request.POST.get("drug_prescription")
        medication.drug_prescription = drug_pre
        medication.save()
        messages.success(request, "Medication Updated!")
        return redirect(request.META.get("HTTP_REFERER"))
    context = {"medication":medication}
    return render(request, "staff/update_medication.html", context)


def delete_medication(request, med_id):
    medication = Medication.objects.get(id = med_id)
    medication.delete()
    return redirect(request.META.get("HTTP_REFERER"))


def room_occupancies(request):
    room_occupancies = RoomOccupancies.objects.all()
    context = {"room_occupancies":room_occupancies}
    return render(request, "staff/room_occupancies.html", context)


def pay_bill(request, occupant_id):
    occupant = RoomOccupancies.objects.get(id = occupant_id)
    if request.method == "POST":
        full_name = request.POST.get("fullname")
        card_number = request.POST.get("card_number")
        expiry = request.POST.get("expiry")
        cvv = request.POST.get("cvv")
        amount = request.POST.get("amount")
        room_id = request.POST.get("room_id")
        room_obj = Room.objects.get(id = room_id)

        billing = Billing(status=True, amount=amount, occupant_id=occupant)
        billing.save()
        occupant.paid = True
        occupant.save()
        room_obj.status = False
        room_obj.save()
        messages.success(request, "Payment Successful!")
        return redirect(request.META.get("HTTP_REFERER"))
    return render(request, "staff/pay_bill.html", context = {"occupant":occupant})


def view_bills(request):
    bills = Billing.objects.all()
    return render(request, "staff/bills.html", context = {"bills":bills})