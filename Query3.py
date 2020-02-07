import mysql.connector

pid = form['pid'].value
def getSupplierpidDetail(pid):
    try:
        print("<table align = 'center' border><tr><th> SNAME </th><th>Address</th></tr>")
        mydb = mysql.connector.connect(
                  host="localhost",
                  user="proj",
                  passwd="proj",
                  database="SupplyDB"
                )

        cursor = mydb.cursor(buffered=True)
        sql_select_query = """select sname,address from Suppliers, Parts, Catalog where Parts.pid = Catalog.pid AND Catalog.sid = Suppliers.sid AND Catalog.cost = (Select MAX(Catalog1.cost) from Catalog Catalog1 Where Catalog1.pid = Parts.pid) AND Parts.pid = %s"""
        cursor.execute(sql_select_query,(pid,))
        record = cursor.fetchall()
        for row in record:
        print("<tr><td>" + row[0] + "</td><td>" + row[1]  "</td>")

            
            
            

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

   


