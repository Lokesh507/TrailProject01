from django.db import connection
from django.shortcuts import render

from .models import Companies

# Create your views here.


def index(request):
    c_name = 'wipro'
    command = "who got placed in Accenture in the batch 2022"
    command2 = "which student has got the highest package till now"
    command3 = "which student got the highest package in batch 2022"
    command4 = "which student has got the highest package till batch 2022"
    command5 = "who got placed in more than 10 companies in the batch 2022"
    command6 = "did 18031A0554 got a job?"
    command7 = "who got placed in more than 10 companies and less than 15 companies in the batch 2022"
    command8 = "what is the package of 18031A0554"
    command9 = "show me the list of students got job in batch 2022"
    command10 = "what is the average package of Galaxe Solutions till now?"
    command11 = "what is the highest package from Galaxe Solutions"
    command12 = "what is the lowest package from Galaxe Solutions"
    l1 = []
    companies_list = ['Accenture', 'Wipro', 'Galaxe Solutions']
    l2 = ['who', 'how-many', 'which', 'how much']
    l1 = command.split(' ')
    for i in l1:
        if(i.isdigit()):
            x = int(i)
        if(i in l2):
            given_question = i
        if(i in companies_list):
            company_name_given = i
    if(given_question == "who"):
        sql = "SELECT * FROM dashboard_Companies where company_name = '{0}' and batch_no = '{1}' order by roll_no".format(
            company_name_given, x)
        sql2 = Companies.objects.raw(sql)
        c_len = sql2.__len__
    if(given_question == "how-many"):
        sql = "SELECT * FROM dashboard_Companies where company_name = '{0}' and batch_no = '{1}' order by roll_no".format(
            company_name_given, x)
        sql2 = Companies.objects.raw(sql)
        c_len = sql2.__len__
        return render(request, 'index.html', {'c_name': company_name_given, 'c_len': c_len})
    else:
        pass
    return render(request, 'index.html', {'c_data': sql2, 'c_name': company_name_given, 'c_len': c_len})
