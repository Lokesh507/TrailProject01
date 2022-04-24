from django.db import connection
from django.shortcuts import render
from re import search
from .models import Companies, DemoDatabase, TrailDatabase07
from django.http import HttpResponse, HttpResponseRedirect
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
    companies_name = []
    batches = []
    reg_nos = []
    questions = ['who', 'how many', 'which']
    packages = ['more than', 'less than',
                'highest', 'least', 'above', 'below']
    keywords = ['till', 'until now']
    all_obj = TrailDatabase07.objects.all()
    for i in all_obj:
        companies_name.append(i.company_name)
        batches.append(i.batch_no)
        reg_nos.append(i.roll_no)

    print(companies_name)
    print(batches)
    print(reg_nos)

    regno_set = set(reg_nos)
    roll_nos = list(regno_set)
#    print(roll_nos)

    query_given = request.POST["query"]
    #query_given = query_given.lower()

    for i in questions:
        if(search(i, query_given)):
            question_keyword = i
        else:
            question_keyword = 'none'

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

    reg_no_count = 0
    for i in roll_nos:
        if(search(i, query_given)):
            reg_no_keyword = i
            reg_no_count = 1

    print(reg_no_count)
    # print(question_keyword)
    if(question_keyword == "who" or question_keyword == "none" or question_keyword == "which" or question_keyword == "how many"):
        if(reg_no_count == 1 and batch_count == 0 and package_count == 0 and keyword_count == 0 and company_count == 0):
            sql_query = "SELECT * FROM dashboard_TrailDatabase07 where roll_no = '{0}' order by roll_no".format(
                reg_no_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed0.....")
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(company_count == 0 and batch_count == 1 and package_count == 0 and keyword_count == 0):
            sql_query = "SELECT * FROM dashboard_TrailDatabase07 where batch_no = '{0}' order by roll_no".format(
                batch_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed1.....")
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(company_count == 1 and batch_count == 0 and package_count == 0 and keyword_count == 0):
            sql_query = "SELECT * FROM dashboard_TrailDatabase07 where company_name = '{0}' order by roll_no".format(
                company_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed1.....")
            return render(request, 'index.html', {'command': query_given, 'c_name': company_keyword, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and company_count == 1 and package_count == 0 and keyword_count == 0):
            sql_query = "SELECT * FROM dashboard_TrailDatabase07 where company_name = '{0}' and batch_no = '{1}' order by roll_no".format(
                company_keyword, batch_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed2.....")
            return render(request, 'index.html', {'command': query_given, 'c_name': company_keyword, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 0 and company_count == 0 and package_count == 1 and keyword_count == 0):
            if(package_keyword == 'above' or package_keyword == 'more than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_TrailDatabase07 WHERE COMPANIES_COUNT > '{0}' ".format(
                    no_of_companies)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed3.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'below' or package_keyword == 'less than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_TrailDatabase07 WHERE COMPANIES_COUNT < '{0}' ".format(
                    no_of_companies)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed4.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'highest' or package_keyword == "higher"):
                sql_query = "select * from dashboard_TrailDatabase07 where salary=(select max(salary) from dashboard_TrailDatabase07)"
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed5.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least' or package_keyword == "lesser"):
                sql_query = "select * from dashboard_TrailDatabase07 where salary=(select min(salary) from dashboard_TrailDatabase07)"
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed6.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and company_count == 1 and package_count == 1 and keyword_count == 0):
            if(package_keyword == 'highest'):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND COMPANY_NAME = '{1}') ORDER BY ROLL_NO".format(
                    batch_keyword, company_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed7.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least'):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MIN(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND COMPANY_NAME = '{1}') ORDER BY ROLL_NO".format(
                    batch_keyword, company_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed8.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and keyword_count == 1 and package_count == 1 and company_count == 0):
            if(package_keyword == 'highest'):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed10.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least'):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}' AND SALARY = (SELECT MIN(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed11.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and keyword_count == 1 and package_count == 1 and company_count == 1):
            sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}' AND  COMPANY_NAME = '{1}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}'  AND  COMPANY_NAME = '{1}') ORDER BY ROLL_NO".format(
                batch_keyword, company_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed12.....")
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and keyword_count == 1 and package_count == 0 and company_count == 1):
            sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO <= '{0}' AND  COMPANY_NAME = '{1}' ORDER BY ROLL_NO".format(
                batch_keyword, company_keyword)
            sql_output = TrailDatabase07.objects.raw(sql_query)
            sql_len = sql_output.__len__
            print("Loop Executed13.....")
            return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 1 and company_count == 0 and package_count == 1 and keyword_count == 0):
            if(package_keyword == "highest"):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MAX(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

            if(package_keyword == "least"):
                sql_query = "SELECT * FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}' AND SALARY = (SELECT MIN(SALARY) FROM DASHBOARD_TrailDatabase07 WHERE BATCH_NO = '{0}') ORDER BY ROLL_NO".format(
                    batch_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})

        if(batch_count == 0 and company_count == 1 and package_count == 1):
            if(package_keyword == 'above' or package_keyword == 'more than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_TrailDatabase07 WHERE COMPANIES_COUNT > '{0}' ".format(
                    no_of_companies)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed14.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'below' or package_keyword == 'less than'):
                for i in range(1, 50):
                    i = str(i)
                    if(search(i, query_given)):
                        no_of_companies = i
                sql_query = "SELECT * FROM dashboard_TrailDatabase07 WHERE COMPANIES_COUNT < '{0}' ".format(
                    no_of_companies)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed15.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'highest' or package_keyword == "higher"):
                sql_query = "select * from dashboard_TrailDatabase07 where salary=(select max(salary) from dashboard_TrailDatabase07 where company_name = '{0}')".format(
                    company_keyword)
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed16.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
            if(package_keyword == 'least' or package_keyord == "lesser"):
                sql_query = "select * from dashboard_TrailDatabase07 where salary=(select min(salary) from dashboard_TrailDatabase07)"
                sql_output = TrailDatabase07.objects.raw(sql_query)
                sql_len = sql_output.__len__
                print("Loop Executed17.....")
                return render(request, 'index.html', {'command': query_given, 'c_len': sql_len, 'c_data': sql_output})
        else:
            print("No Loop executed")
            return render(request,'error_redirect_page.html',{'query':query_given})


def entry(request):
    if(request.method == "POST"):
        roll_no = request.POST["reg_no"]
        student_name = request.POST["student_name"]
        company_name = request.POST["company_name"]
        batch_no = request.POST["batch_no"]
        salary_package = request.POST["package"]

        if(TrailDatabase07.objects.filter(roll_no=roll_no).exists()):
            print("Founded a Record")
            sql_query1_first = "SELECT id,max(companies_count) FROM DASHBOARD_TrailDatabase07 WHERE roll_no = '{0}' group by id".format(
                roll_no)
            print("Printing.....")
            for s in TrailDatabase07.objects.raw(sql_query1_first):
                print(s.companies_count)
                company_count = s.companies_count + 1
            TrailDatabase07_obj = TrailDatabase07(
                roll_no=roll_no, s_name=student_name, company_name=company_name, batch_no=batch_no, salary=salary_package, companies_count=company_count)
            TrailDatabase07_obj.save()
            update_obj = TrailDatabase07.objects.all().filter(roll_no=roll_no)
            for l in update_obj:
                l.companies_count = company_count
                l.save()

        else:
            print("New Record")
            company_count = 1
            TrailDatabase07_obj = TrailDatabase07(
                roll_no=roll_no, s_name=student_name, company_name=company_name, batch_no=batch_no, salary=salary_package, companies_count=company_count)
            TrailDatabase07_obj.save()
        # return HttpResponse("Data Submitted Successfully....")
        return HttpResponseRedirect('post_data')
    else:
        return render(request, 'register.html')


def index_page(request):
    return render(request, 'home.html')


def login_page(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'register.html')
