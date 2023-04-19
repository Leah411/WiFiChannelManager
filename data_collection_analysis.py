# import serial
# import csv
#
# # Define the serial port settings
# ser = serial.Serial('COM3', 115200)
#
# # Open a new CSV file for writing
# csv_file = open('data.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)
#
# # Write the header row to the CSV file
# csv_writer.writerow(['Time', 'Value'])
#
# # Use a loop to read data from the serial port and write it to the CSV file
# while True:
#     # Read a line of data from the serial port
#     data = ser.readline().decode().strip()
#
#     # Split the data into separate values
#     values = data.split(',')
#
#     # Write the values to the CSV file
#     csv_writer.writerow(values)
#
#     # Print the values to the console
#     print(values)
#
# # Close the CSV file and the serial port once you are finished collecting data
# csv_file.close()
# ser.close()