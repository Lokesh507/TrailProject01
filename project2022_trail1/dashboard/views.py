from django.db import connection
from django.shortcuts import render
from re import search
from .models import Companies, DemoDatabase

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


def home(request):
    companies_name = ['wipro', 'GalaxE Solutions', 'tcs', 'accenture', 'atai']
    questions = ['who', 'how many', 'which']
    batches = ['2022', '2021', '2020']
    packages = ['more than', 'less than',
                'highest', 'least', 'above', 'below']
    reg_nos = ['18031A0507', '18031A0544', '18031A0505', '18031A0504']
    keywords = ['till', 'until now']

    query_given = "who got the least package till batch 2022?"

    for i in questions:
        if(search(i, query_given)):
            question_keyword = i
    company_count = 0
    for i in companies_name:
        if(search(i, query_given)):
            company_keyword = i
            company_count = 1

    batch_count = 0
    for i in batches:
        if(search(i, query_given)):
            batch_keyword = i
            batch_count = 1

    package_count = 0
    for i in packages:
        if(search(i, query_given)):
            package_keyword = i
            package_count = 1

    keyword_count = 0
    for i in keywords:
        if(search(i, query_given)):
            keyword_keyword = i
            keyword_count = 1

    print(package_keyword)

    if(question_keyword == 'who'):
        if(company_count == 1 and batch_count == 0 and package_count == 0 and keyword_count == 0):
            sql_query = "SELECT * FROM dashboard_DemoDatabase where company_name = '{0}' order by roll_no".format(
                company_keyword)
            sql_output = DemoDatabase.objects.raw(sql_query)
            sql_len = sql_output.__len__
            return render(request, 'index.html', {'command': query_given, 'c_name': company_keyword, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 1 and company_count == 1 and package_count == 0 and keyword_count == 0):
            sql_query = "SELECT * FROM dashboard_DemoDatabase where company_name = '{0}' and batch_no = '{1}' order by roll_no".format(
                company_keyword, batch_keyword)
            sql_output = DemoDatabase.objects.raw(sql_query)
            sql_len = sql_output.__len__
            return render(request, 'index.html', {'command': query_given, 'c_name': company_keyword, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 0 and company_count == 0 and package_count == 1 and keyword_count == 0):
            if(package_keyword == 'above' or package_keyword == 'more than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_DemoDatabase WHERE COMPANIES_COUNT > '{0}' ".format(
                    no_of_companies)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'below' or package_keyword == 'less than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_DemoDatabase WHERE COMPANIES_COUNT < '{0}' ".format(
                    no_of_companies)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'highest'):
                sql_query = "select * from dashboard_DemoDatabase where salary=(select max(salary) from dashboard_DemoDatabase)"
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least'):
                sql_query = "select * from dashboard_DemoDatabase where salary=(select min(salary) from dashboard_DemoDatabase)"
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 1 and company_count == 0 and package_count == 1 and keyword_count == 0):
            if(package_keyword == 'highest'):
                sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least'):
                sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MIN(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 1 and company_count == 1 and package_count == 1 and keyword_count == 0):
            sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}' AND COMPANY_NAME = '{1}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO = '{0}' AND COMPANY_NAME = '{1}') ORDER BY ROLL_NO".format(
                batch_keyword, company_keyword)
            sql_output = DemoDatabase.objects.raw(sql_query)
            sql_len = sql_output.__len__
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 1 and keyword_count == 1 and package_count == 1 and company_count == 0):
            if(package_keyword == 'highest'):
                sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least'):
                sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}' AND SALARY = (SELECT MIN(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = DemoDatabase.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
        if(batch_count == 1 and keyword_count == 1 and package_count == 1 and company_count == 1):
            sql_query = "SELECT * FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}' AND  COMPANY_NAME = '{1}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_DEMODATABASE WHERE BATCH_NO <= '{0}'  AND  COMPANY_NAME = '{1}') ORDER BY ROLL_NO".format(
                batch_keyword, company_keyword)
            sql_output = DemoDatabase.objects.raw(sql_query)
            sql_len = sql_output.__len__
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
