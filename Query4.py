import mysql.connector

color = form['color'].value
address = form['address'].value
def getPartsDetail(color, address):
    try:
        print("<table align = 'center' border><tr><th> PNAME </th></tr>")
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="proj",
                  passwd="proj",
                  database="SupplyDB"
                )
        colorAddress = (color,address,address,color,color,address)
        cursor = mydb.cursor(buffered=True)
        sql_select_query = """Select pname from Parts, Suppliers where color = %s AND address = %s AND NOT EXISTS
(Select distinct Suppliers.sid from Catalog, Suppliers, Parts where address = %s AND color = %s AND Suppliers.sid NOT IN
(Select Catalog.sid from Parts, Catalog, Suppliers Where color = %s AND address = %s AND Parts.pid = Catalog.pid AND Catalog.sid = Suppliers.sid))"""
        cursor.execute(sql_select_query,colorAddress)
        record = cursor.fetchall()

        
        for row in record:
            print("<tr><td>" + row[0] + "</td>")
            
            
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

