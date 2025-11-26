import cherrypy
import mysql.connector

def getConnection():
    return mysql.connector.connect(host="localhost",user="root",password="",database="newone")

class MyApp:
    # read method
    @cherrypy.expose
    def index(self):
        conn = getConnection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM staff")
        row = cur.fetchall()
        conn.close()
        output = "<h2>List Items</h2>"
        for r in row:
            output += f"{r[0]} - {r[1]}<br>"
        return output
cherrypy.config.update({'server.socket_port': 9090})
cherrypy.quickstart(MyApp(),"/",config={})