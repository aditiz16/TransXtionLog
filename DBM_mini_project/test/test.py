import mysql.connector as sql
username='aditi_z'
email='aditizeminder2003@gmail.com'
password='123'
confirm_password='123'
# Create your views here.
# global username,email,password,confirm_password
# if request.method=="POST":
obj=sql.connect(host="localhost",user="root",passwd="admin",database='dbmminiproj')
cursor=obj.cursor()
# data=request.POST
data={'username':username,'email':email,'password':password,'confirm-password':confirm_password}
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