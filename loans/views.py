# from django.http import HttpResponse
# from .models import RepaymentSchedule, LoanList
# from django.views.decorators.csrf import csrf_exempt
# from django.db import transaction
# from datetime import datetime
# from dateutil import relativedelta

# @csrf_exempt 

# def get_listings_or_add_loan(request):
#     if request.method == 'POST':
#         # If POST request where data is to be saved in two tables, use a database transaction
#         with transaction.atomic():
#             loan_amount_int = int(request.POST['loan_amount'])
#             loan_term_int = int(request.POST['loan_term'])
#             interest_rate_int = float(request.POST['interest_rate'])
#             loan_date =   datetime.today()
#             new_loan = LoanList(
#                 loan_amount = loan_amount_int, 
#                 loan_term = loan_term_int, 
#                 interest_rate = interest_rate_int, 
#                 ) 
#             new_loan.save()
#             print('post request done')
#             print(LoanList.objects.all())
#             calculate_repayment(loan_amount_int, loan_term_int, interest_rate_int,  loan_date, new_loan)
#             return HttpResponse("hi!")
#     elif request.method == 'GET':
#         loan_list = LoanList.objects.all()
#         print('get all done')
#         print(datetime.today())
#         return HttpResponse(loan_list)

# def calculate_repayment(loan_amount, loan_term, interest_rate_percentage, loan_date, new_loan):
#     interest_rate = interest_rate_percentage / 100
#     pmt = loan_amount * (interest_rate/12) / (1 - ((1 + (interest_rate/12)) ** (-12 * loan_term)))
#     no_of_months = loan_term * 12
#     balance = loan_amount

#     repayment_list = []
#     for x in range(1, no_of_months + 1):
#         if x == no_of_months + 1:
#             monthly_interest = (interest_rate / 12) * balance
#             prinicipal = balance - monthly_interest
#             balance = 0
#         else:
#             monthly_interest = (interest_rate / 12) * balance
#             prinicipal = pmt - monthly_interest
#             balance = balance - prinicipal
#         repayment_list.append(RepaymentSchedule(
#             loan_id = new_loan,
#             payment_no = x,
#             date =  loan_date + relativedelta.relativedelta(months=x),
#             payment_amount = pmt,
#             prinicipal = prinicipal,
#             interest = monthly_interest,
#             balance = balance
#         ))
#     RepaymentSchedule.objects.bulk_create(repayment_list)

#     print('testing') 

# def get_listing_and_repayment(request, listing_id):
#     if request.method == 'GET':
#         loan_details = LoanList.objects.get(id=listing_id)
#         repayment_details = RepaymentSchedule.objects.filter(loan_id_id__id = listing_id)
#         print('get')
#         print(loan_details)
#         print(repayment_details)
#         return HttpResponse({loan_details, repayment_details})
#     elif request.POST['action'] == 'DELETE':
#         print('delete working')


from django.http import HttpResponse
from .models import RepaymentSchedule, LoanList
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from datetime import datetime
from dateutil import relativedelta

@csrf_exempt 

def get_listings_or_add_loan(request):
    if request.method == 'POST':
        # If POST request where data is to be saved in two tables, use a database transaction
        with transaction.atomic():
            loan_amount_int = int(request.POST['loan_amount'])
            loan_term_int = int(request.POST['loan_term'])
            interest_rate_int = float(request.POST['interest_rate'])
            loan_date =   datetime.today()
            new_loan = LoanList(
                loan_amount = loan_amount_int, 
                loan_term = loan_term_int, 
                interest_rate = interest_rate_int, 
                ) 
            new_loan.save()
            print('post request done')
            print(LoanList.objects.all())
            calculate_repayment(loan_amount_int, loan_term_int, interest_rate_int,  loan_date, new_loan)
            return HttpResponse("hi!")
    elif request.method == 'GET':
        loan_list = LoanList.objects.all()
        print('get all done')
        print(datetime.today())
        return HttpResponse(loan_list)

def calculate_repayment(loan_amount, loan_term, interest_rate_percentage, loan_date, new_loan):
    interest_rate = interest_rate_percentage / 100
    pmt = loan_amount * (interest_rate/12) / (1 - ((1 + (interest_rate/12)) ** (-12 * loan_term)))
    no_of_months = loan_term * 12
    balance = loan_amount

    repayment_list = []
    for x in range(1, no_of_months + 1):
        if x == no_of_months + 1:
            monthly_interest = (interest_rate / 12) * balance
            prinicipal = balance - monthly_interest
            balance = 0
        else:
            monthly_interest = (interest_rate / 12) * balance
            prinicipal = pmt - monthly_interest
            balance = balance - prinicipal
        repayment_list.append(RepaymentSchedule(
            loan_id = new_loan,
            payment_no = x,
            date =  loan_date + relativedelta.relativedelta(months=x),
            payment_amount = pmt,
            prinicipal = prinicipal,
            interest = monthly_interest,
            balance = balance
        ))
    RepaymentSchedule.objects.bulk_create(repayment_list)

    print('testing') 

def get_listing_and_repayment(request, listing_id):
    if request.method == 'GET':
        loan_details = LoanList.objects.get(id=listing_id)
        repayment_details = RepaymentSchedule.objects.filter(loan_id_id__id = listing_id)
        print('get')
        print(loan_details)
        print(repayment_details)
        return HttpResponse({loan_details, repayment_details})
    elif request.POST['action'] == 'DELETE':
        print('delete working')
