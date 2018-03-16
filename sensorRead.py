import sqlite3
import serial
from datetime import datetime


#Serial Conexion with Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
print('Read Serial');
#print(arduino);
i=0
light = 0
hum = 0
temp = 0
#Used for synch of values
valor = '2000';
a = '111111'
bandera = 0;
#1000 values of the sensors are read. To read indeterminately change for (while 1:)
#Data is read in 4 states
while i<1000:
    #Leer Datos
    a = arduino.readline();
    #print(a);
    a = (a.split())[0];
    #print(type(valor));
    if a==valor and bandera==0:
        bandera = 1;
        #print('Recibi valores de sensores');
    elif bandera==1:
        light = a;
        bandera = 2;
    elif bandera==2:
        hum = a;
        bandera=3;
    else:
        temp = a;
        #Los valores han sido leidos totalmente y se llevan a la pagina y guardan en una base de datos
        i=i+1;
        bandera = 0;
	print("Light %s   Temp %s   Hum%s" % (light,temp,hum));

        #This lines allow updating information to the database

        conn = sqlite3.connect('datos.db');
        conn.text_factory = str;
        c = conn.cursor();
        sqlQuery = 'INSERT INTO sensors VALUES (?, ?, ?, ? )';
        #print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]);
        c.execute(sqlQuery, (light,hum,temp,datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]));
        conn.commit();
        conn.close();

        #Create web page -> Write directly HTML
        print("Creating web page");

        F = open("./html/index2.html", "w");
        #print (F);
        F.write("<!DOCTYPE html>");
        F.write("<<!-- greet.html A trivial HTML5 document -->");
	    F.write("<head>");
        F.write('''<meta http-equiv="refresh" content="1">''');
        F.write("<title> Proyecto IoT </title>");
        F.write("</head>");
        F.write("<body>");
        F.write("<h1>Proyecto IoT</h1>");
        F.write("<p>Oscar Castelblanco - Camila Alvarez - Laura Ramos</p>");
        F.write("<p> Sensor ");
        F.write("Light :");
        F.write(repr(light)+"</p>");
        F.write("<p> Sensor ");
        F.write("Temperature:");
        F.write(repr(temp)+"</p>");
        F.write("<p> Sensor ");
        F.write("Humidity :");
        F.write(repr(hum)+"</p>");
        F.write("</body>");
        F.write("</html>");
        F.close();
arduino.close()
