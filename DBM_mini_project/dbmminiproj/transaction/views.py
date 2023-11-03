from django.shortcuts import render
import mysql.connector as sql
transactionid=''
customerId=''
amount=''
date=''
# Create your views here.
def transaction_action(request):
    global transactionid,customerId,amount,date
    if request.method=="POST":
        obj=sql.connect(host="localhost",user="root",passwd="admin",database='dbmminiproj')
        cursor=obj.cursor()
        data=request.POST
        for key,value in data.items():
            if key=="CustomerID":
                customerId=value
            if key=="TransactionID":
                transactionid=value
            if key=="Amount":
                amount=value
            if key=="date":
                date=value
        query="insert into users values('{}','{}','{}','{}')".format(customerId,transactionid,amount,date)
        cursor.execute(query)
        obj.commit()
    return render(request,'transaction_page.html')