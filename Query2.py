import mysql.connector
import mysql.connector

cost = form['cost'].value
def getSuppliercostDetail(cost):
    try:
        print("<table align = 'center' border><tr><th> SNAME </th></tr>" )
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="proj",
                  passwd="proj",
                  database="SupplyDB"
                )

        cursor = mydb.cursor(buffered=True)
        sql_select_query = """select distinct sname from Suppliers, Catalog where Suppliers.sid = Catalog.sid AND cost >= %s"""
        cursor.execute(sql_select_query, (cost,))
        record = cursor.fetchall()

        for row in record:
        print("<tr><td>" + row[0] + "</td>")
        
            
            
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

   


