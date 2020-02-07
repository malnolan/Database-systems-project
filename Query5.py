import mysql.connector

address = form['address2'].value
def getSupplieraddressDetail(address):
    try:
        print("<table align = 'center' border><tr><th> SNAME </th></tr>" )
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="proj",
                  passwd="proj",
                  database="SupplyDB"
                )

        cursor = mydb.cursor(buffered=True)
        sql_select_query = """select sname from Suppliers where address = %s AND Suppliers.sid NOT IN (select distinct Suppliers.sid From Catalog, Suppliers Where Catalog.sid = Suppliers.sid)"""
        cursor.execute(sql_select_query,(address,))
        record = cursor.fetchall()
        for row in record:
            print("<tr><td>" + row[0] + "</td>")
           
            
            
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

   


