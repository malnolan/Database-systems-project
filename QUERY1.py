import mysql.connector

pname = form['pname'].value
def getSupplierDetail(pname):
    try:
        print("<table align = 'center' border><tr><th> SID </th><th> SNAME </th> <th>Address</th><th>Cost</th></tr>")
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="proj",
                  passwd="proj",
                  database="SupplyDB"
                )

        cursor = mydb.cursor(buffered=True)
        sql_select_query = """select distinct Suppliers.sid,sname,address,cost from Suppliers, Parts, Catalog where Suppliers.sid = Catalog.sid AND Catalog.pid = Parts.pid AND Parts.pname = %s"""
        cursor.execute(sql_select_query, (pname,))
        record = cursor.fetchall()

        for row in record:
            print("<tr><td>" + row[0] + "</td><td>" + row[1]  "</td><td>" + row[2] "</td><td>" + row[3] "</td>")
    
            
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

   




