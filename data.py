import serial
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import datetime

#Tilføjer tid
curret_time = datetime.datetime.now()

time = curret_time.strftime("%Y-%m-%d %H:%M:%S")

# Define the serial port for each Arduino #'/dev/cu.usbmodem11431101'','/dev/cu.usbmodem11441101'
arduino_ports = ['/dev/cu.usbmodem1142401','/dev/cu.usbmodem1141401','/dev/cu.usbmodem11431101','/dev/cu.usbmodem11441101']  # Adjust these to match your setup

# Open a serial connection to each Arduino
arduino_connections = [serial.Serial(port, 9600) for port in arduino_ports]

nummer = 0

sensor_numre0 = []
sensor_numre1 = []
sensor_numre2 = []
sensor_numre3 = []

print(f"Måling startet {time}")


while True:
    for i, connection in enumerate(arduino_connections):
        
        # Read data from the Arduino
        data = connection.readline().decode('utf-8').strip()
        
        values = data.split(',')
        
        if values[0] == "TID" and i==1:
            nummer += 1
            #Nummer på sensorer
            for m in range(0,len(values)):
                for l in range(0,8):
                    if values[m] == f"C02_{l}" :
                        sensor_numre1.append(l)
            print(f"Arduino {i+1} er fundet")
            print(f"Følgende sensorer er tilsluttede {sensor_numre1}")
        
        if values[0] == "TID" and i==0:
            nummer += 1
            #Nummer på sensorer
            for m in range(0,len(values)):
                for l in range(0,8):
                    if values[m] == f"C02_{l}" :
                        sensor_numre0.append(l)
            print(f"Arduino {i+1} er fundet")
            print(f"Følgende sensorer er tilsluttede {sensor_numre0}")
        
        if values[0] == "TID" and i==2:
            nummer += 1
            #Nummer på sensorer
            for m in range(0,len(values)):
                for l in range(0,8):
                    if values[m] == f"C02_{l}" :
                        sensor_numre2.append(l)
            print(f"Arduino {i+1} er fundet")
            print(f"Følgende sensorer er tilsluttede {sensor_numre2}")

        if values[0] == "TID" and i==3:
            nummer += 1
            #Nummer på sensorer
            for m in range(0,len(values)):
                for l in range(0,8):
                    if values[m] == f"C02_{l}" :
                        sensor_numre3.append(l)
            print(f"Arduino {i+1} er fundet")
            print(f"Følgende sensorer er tilsluttede {sensor_numre3}")
        
        if nummer == len(arduino_ports):
            break
    if nummer == len(arduino_ports):
        break

for connection in arduino_connections:
    connection.close()
    
arduino_connections = [serial.Serial(port, 9600) for port in arduino_ports]

# Create CSV files for each Arduino
csv_files = [open(f'data_arduino_{i}.csv', 'w', newline='') for i in range(1, len(arduino_ports) + 1)]
csv_writers = [csv.writer(csv_file, delimiter=',') for csv_file in csv_files]


# Create a figure and axis for plotting
fig, ax = plt.subplots(len(arduino_ports), 2, sharex=True)



# Initialize empty plots for each Arduino
plots0 = [ax[0,0].plot([], [], label=f"Sensor {sensor_numre0[j]}")[0] for j in range(len(sensor_numre0))]
plots1 = [ax[1,0].plot([], [], label=f"Sensor {sensor_numre1[j]}")[0] for j in range(len(sensor_numre1))]
plots2 = [ax[2,0].plot([], [], label=f"Sensor {sensor_numre2[j]}")[0] for j in range(len(sensor_numre2))]
plots3 = [ax[3,0].plot([], [], label=f"Sensor {sensor_numre3[j]}")[0] for j in range(len(sensor_numre3))]


tempplot0 = [ax[0,1].plot([], [], label=f"Sensor {sensor_numre0[j]}")[0] for j in range(len(sensor_numre0))]
tempplot1 = [ax[1,1].plot([], [], label=f"Sensor {sensor_numre1[j]}")[0] for j in range(len(sensor_numre1))]
tempplot2 = [ax[2,1].plot([], [], label=f"Sensor {sensor_numre2[j]}")[0] for j in range(len(sensor_numre2))]
tempplot3 = [ax[3,1].plot([], [], label=f"Sensor {sensor_numre3[j]}")[0] for j in range(len(sensor_numre3))]

co2_ax = ax[:,0]
temp_ax = ax[:,1]

# Set labels, titles, and legend for each subplot
for i, axis in enumerate(co2_ax):
    axis.set_ylabel('$CO_2$ (ppm)')
    axis.legend(loc='center left')
    axis.set_title(f'Arduino {i + 1}')  # Add this line to set the title

for i, axis in enumerate(temp_ax):
    axis.set_ylabel('Temperatur ($C\degree$)')
    axis.legend(loc='center left')
    axis.set_title(f'Arduino {i + 1}')  # Add this line to set the title

# Start for variabler
Dataopsamling0 = False
Dataopsamling1 = False
Dataopsamling2 = False
Dataopsamling3 = False


#For arduino 1
co2_data = [[] for _ in range(8)]
x_data = [[] for _ in range(8)]
temperatur_data1 = [[] for _ in range(8)]


#For arduino 0
co2_data0 = [[] for _ in range(8)]
temperatur_data0 = [[] for _ in range(8)]
x_data0 = [[] for _ in range(8)]



#For arduino 3
temperatur_data2 = [[] for _ in range(8)]
x_data2 = [[] for _ in range(8)]
co2_data2 = [[] for _ in range(8)]


#For arduino 4
temperatur_data3 = [[] for _ in range(8)]
x_data3 = [[] for _ in range(8)]
co2_data3 = [[] for _ in range(8)]





# Define the update function for animation
def update(frame):
    try:
        for i, connection in enumerate(arduino_connections):
            global Dataopsamling1, co2_data, x_data, sensor_numre0, sensor_numre1
            global sensor_numre2, sensor_numre3, Dataopsamling0, Dataopsamling2, Dataopsamling3
            # Read data from the Arduino
            data = connection.readline().decode('utf-8').strip()
            
            
            # Split the data into a list of values and write it to the CSV file
            values = data.split(',')
            
            
                
            
# =============================================================================
#           Sensor 1  
# =============================================================================
            if values[0] == "TID" and i == 1:
                Dataopsamling1 = True
                
                
                print("Data opsamles for 2")
                
                csv_writers[i].writerow(["Måling startet", time.replace(',', '')])

            if Dataopsamling1 and values[0] != "TID":
                if i == 1:

                    # Lav list til resultat
                    resultat = [p for p in range(0, len(values))]

                    # Undersøger for NaN og værdier
                    if values[0] != "TID":
                        if values[0] == "NaN":
                            pass
                        
                        elif eval(values[0])>800:
                            for b in range(0, len(values)):
                                if values[b] == "NaN":
                                    resultat[b] = None
                                else:
                                    resultat[b] = eval(values[b])
    
                            x_data[i].append(resultat[0]/1000)
        
                            co2 = [resultat[m] for m in range(1, len(values), 2)]
                            temperatur = [resultat[m] for m in range(2, len(values), 2)]
                            
                            for sensor_num in range(len(sensor_numre1)):
                                temperatur_data1[sensor_num].append(temperatur[sensor_num])
                                tempplot1[sensor_num].set_data(x_data[i], temperatur_data1[sensor_num])
                            
                            for sensor_num in range(len(sensor_numre1)):
                                co2_data[sensor_num].append(co2[sensor_num])
                                plots1[sensor_num].set_data(x_data[i], co2_data[sensor_num])
        
                            ax[i,0].relim()
                            ax[i,0].autoscale_view()
                            ax[i,1].relim()
                            ax[i,1].autoscale_view()
                            
                            



# ============================================================================
#           Sensor 0 
# =============================================================================
            if values[0] == "TID" and i == 0:
                Dataopsamling0 = True
                
                print("Data opsamles for 1")
                
                csv_writers[i].writerow(["Måling startet", time.replace(',', '')])

            if Dataopsamling0 and values[0] != "TID":
                if i == 0:

                    # Lav list til resultat
                    resultat = [p for p in range(0, len(values))]

                    # Undersøger for NaN og værdier
                    if values[0] != "TID": 
                        if values[0] == "NaN":
                            pass
                        
                        elif eval(values[0])>800:
                            for b in range(0, len(values)):
                                if values[b] == "NaN":
                                    resultat[b] = None
                                else:
                                    resultat[b] = eval(values[b])
    
                            x_data0[i].append(resultat[0]/1000)
        
                            co2 = [resultat[m] for m in range(1, len(values), 2)]
                            
                            temperatur = [resultat[m] for m in range(2, len(values), 2)]
                            
                            for sensor_num in range(len(sensor_numre0)):
                                 temperatur_data0[sensor_num].append(temperatur[sensor_num])
                                 tempplot0[sensor_num].set_data(x_data0[i], temperatur_data0[sensor_num])
                            
                            for sensor_num in range(len(sensor_numre0)):
                                co2_data0[sensor_num].append(co2[sensor_num])
                                plots0[sensor_num].set_data(x_data0[i], co2_data0[sensor_num])
        
                            ax[i,0].relim()
                            ax[i,0].autoscale_view()
                            ax[i,1].relim()
                            ax[i,1].autoscale_view()

# =============================================================================
#           Sensor 2
# =============================================================================
            if values[0] == "TID" and i == 2:
                Dataopsamling2 = True
                
                print("Data opsamles for 3")
                
                csv_writers[i].writerow(["Måling startet", time.replace(',', '')])

            if Dataopsamling2 == True and values[0] != "TID":
                if i == 2:

                    # Lav list til resultat
                    resultat = [p for p in range(0, len(values))]

                    # Undersøger for NaN og værdier
                    if values[0] != "TID":
                        
                        if values[0] == "NaN":
                            pass
                        
                        elif eval(values[0])>800:    
                            for b in range(0, len(values)):
                                if values[b] == "NaN":
                                    resultat[b] = None
                                else:
                                    resultat[b] = eval(values[b])
    
                            x_data2[i].append(resultat[0]/1000)
        
                            co2 = [resultat[m] for m in range(1, len(values), 2)]
                            
                            temperatur = [resultat[m] for m in range(2, len(values), 2)]
                            
                            for sensor_num in range(len(sensor_numre2)):
                                temperatur_data2[sensor_num].append(temperatur[sensor_num])
                                tempplot2[sensor_num].set_data(x_data2[i], temperatur_data2[sensor_num])
                            
                            for sensor_num in range(len(sensor_numre2)):
                                co2_data2[sensor_num].append(co2[sensor_num])
                                plots2[sensor_num].set_data(x_data2[i], co2_data2[sensor_num])
        
                            ax[i,0].relim()
                            ax[i,0].autoscale_view()
                            ax[i,1].relim()
                            ax[i,1].autoscale_view()

# =============================================================================
#           Sensor 3
# =============================================================================
            if values[0] == "TID" and i == 3:
                Dataopsamling3 = True
                
                print("Data opsamles for 4")
                
                csv_writers[i].writerow(["Måling startet", time.replace(',', '')])

            if Dataopsamling3 == True and values[0] != "TID":
                if i == 3:

                    # Lav list til resultat
                    resultat = [p for p in range(0, len(values))]

                    # Undersøger for NaN og værdier
                    if values[0] != "TID":
                        
                        if values[0] == "NaN":
                            pass
                        
                        elif eval(values[0])>800:
                            
                            for b in range(0, len(values)):
                                if values[b] == "NaN":
                                    resultat[b] = None
                                else:
                                    resultat[b] = eval(values[b])
    
                            x_data3[i].append(resultat[0]/1000)
        
                            co2 = [resultat[m] for m in range(1, len(values), 2)]
                            
                            temperatur = [resultat[m] for m in range(2, len(values), 2)]
                            
                            for sensor_num in range(len(sensor_numre3)):
                                temperatur_data3[sensor_num].append(temperatur[sensor_num])
                                tempplot3[sensor_num].set_data(x_data3[i], temperatur_data3[sensor_num])
                            
                            for sensor_num in range(len(sensor_numre3)):
                                co2_data3[sensor_num].append(co2[sensor_num])
                                plots3[sensor_num].set_data(x_data3[i], co2_data3[sensor_num])
        
                            ax[i,0].relim()
                            ax[i,0].autoscale_view()
                            ax[i,1].relim()
                            ax[i,1].autoscale_view()
        
            csv_writers[i].writerow(values)


    except KeyboardInterrupt:
        for connection in arduino_connections:
            connection.close()
        for csv_file in csv_files:
            csv_file.close()
        plt.close()  # Close the plot window
        print("Script terminated by user.")

# Create the animation
ani = FuncAnimation(fig, update, blit=False)

try:
    plt.show()
except KeyboardInterrupt:
    for connection in arduino_connections:
        connection.close()
    for csv_file in csv_files:
        csv_file.close()
    print("Script terminated by user.")

