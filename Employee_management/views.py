from django.http import JsonResponse
from django.shortcuts import render
from .models import Adding, Attendance


# for the home page
def index(request):
    return render(request, 'Employee_management/index.html')


# add the employee
def add(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        # age = request.GET['age']
        destination = request.GET.get('destination')
        date = request.GET.get('date')
        if name and destination:
            Adding.objects.create(name=name, destination=destination, date=date)
            return render(request, 'Employee_management/index.html')
        else:
            return render(request, 'Employee_management/sucess.html')
    else:
        return render(request, 'Employee_management/index.html')


# get all the details as a json
def get_data(request):
    employee_datas = Adding.objects.all()
    # to get all the employee details as a list
    employee_data = list(employee_datas.values('id', 'name', 'destination', 'date'))
    # return all the employee in the form of the json data
    return JsonResponse(employee_data, safe=False)


# receive the data in the specific user
def get_specific_employee(request, id):
    if request.method == 'GET':
        employee_data = Adding.objects.get(id=id)
        json_data = {
            'id': employee_data.id,
            'name': employee_data.name,
            'destination': employee_data.destination,
            'date': employee_data.date,
        }
        return JsonResponse(json_data, safe=False)
    else:
        return render(request,'Employee_management/sucess.html')

# mark the attendance for the specific user
def mark_attendance(request, id, status):
    if request.method == 'GET':
        datas = ['Present', 'Absent']
        if status in datas:
            add_db = Adding.objects.get(id=id)
            Attendance.objects.create(employee_id=add_db, status=status)
            return render(request, 'Employee_management/sucess.html')

    else:
        return render(request,'Employee_management/sucess.html')

# get the attendance of all the user
def get_attendance(request):
    if request.method == 'GET':
        attendance = Attendance.objects.all()
        result = list(attendance.values('employee_id', 'date', 'status'))
        return JsonResponse(result, safe=False)

    else:
        return render(request,'Employee_management/sucess.html')

# get the specific dep attendance
def get_specificdep_attendance(request, dep_name):
    if request.method == 'GET':
        attendance_records = Attendance.objects.filter(employee_id__destination=dep_name).values(
            'employee_id__id', 'employee_id__name', 'date', 'status'
        )
        return JsonResponse(list(attendance_records), safe=False)

    else:
        return render(request,'Employee_management/sucess.html')

