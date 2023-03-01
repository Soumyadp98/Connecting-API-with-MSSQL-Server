from django.shortcuts import render
from DjangoApi.models import sqlserverconn
import pyodbc

def connsql(request):
    conn=pyodbc.connect('Driver={SQL Server};Server=ACESWEB;'
                            'Database=dbBSSGhatsila;Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute('select * from T_SPIRITUAL_HARMONY')
    result=cursor.fetchall()
    return render(request,'index.html',{'sqlserverconn':result})