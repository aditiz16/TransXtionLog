from django.shortcuts import render
import mysql.connector as sql
username=''
email=''
password=''
confirm_password=''
# Create your views here.
def signupaction(request):
    global username,email,password,confirm_password
    if request.method=="POST":
        obj=sql.connect(host="localhost",user="root",passwd="admin",database='dbmminiproj')
        cursor=obj.cursor()
        data=request.POST
        for key,value in data.items():
            if key=="username":
                username=value
            if key=="email":
                email=value
            if key=="password":
                password=value
            if key=="confirm-password":
                confirm_password=value
        if password==confirm_password:
            query="insert into users values('{}','{}','{}')".format(username,email,password)
            cursor.execute(query)
            obj.commit()
    return render(request,'signup_page.html')
    
    # return None
