import socket
import csv
import re
meslen = 1000
print("version2 ")

sock = socket.socket()

host = "192.168.101.184" #ESP32 IP in local network
port = 80             #ESP32 Server Port

sock.connect((host, port))
print("connected host and port")
message ='1'.encode('utf_8')
sock.send(message)

data = ""
while len(data) < meslen:
    # print(sock.recv(1))
    a = sock.recv(1)
   # print(ord(a.decode('UTF-8')))
   # print(type(ord(a.decode('UTF-8'))))
   # print(type(ord(a.decode('UTF-8')) > 48))
   # print(type(ord(a.decode('UTF-8')) < 122))
    if((ord(a.decode('UTF-8')) > 41) & (ord(a.decode('UTF-8')) < 122)):
        data += (a.decode('UTF-8'))
    print(data)

print("final data " + data)

sock.close()

## post proccesing

#data = re.sub(r'.', '', data, count = 18)

# Define the path to your output file
output_file = 'output_data.csv'

# Define the character you want to filter by
filter_character = '*'

# the headers for your output file
headers = ['SSID', 'RSSI', 'channel']

# Split the input data into rows using the comma as a separator
rows = data.split('*')
print("split data: ")
print("\n")
print(rows)
rows.pop(0)
rows.pop()
rows.pop()
rows.pop()
print(list(filter(('').__ne__, rows)))

rows = list(filter(('').__ne__, rows))

def chunks(rows, n):
    for i in range(0, len(rows), n):
        yield rows[i:i + n]

#for i in chunks(rows, 3):
   # print(i)


# Open the output file and write the filtered rows
with open(output_file, 'w' , newline='') as f:
    writer = csv.writer(f)
    # Write the headers
    writer.writerow(headers)
    writer.writerows(chunks(rows, 3))

