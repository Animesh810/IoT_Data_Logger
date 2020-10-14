import time
import spidev  #download this library # already downloaded in this machine
import socket

#####################Function Descriptions#######################

def print_csv(ch_num , received_list):
    """
    This function appends the new values into the list
    """
    file_name = "testSPI[{}]"
    delimiter = ','
    with open( file_name.format( ch_num ) , 'a' ) as f:  # the 'a' is for append
        #f.write(json.dumps(time.gmtime()))
        f.write( format(data) )
        f.write(delimiter)
        
    None


#SPI
bus = 1
device = 0 #this is the chip select pin

spi = spidev.SpiDev()
spi.close()
spi.open(bus, device)

#spi.max_speed_hz = 3900000  #working speed 3.9Mhz, 5.4Mhz
spi.max_speed_hz =  2000000
spi.mode = 0

time.sleep(0.005)

time.sleep(1)

#SOCKETS

#host = socket.gethostname();
host = '192.168.1.7' # server IP
port = 12359  # must match server
s = socket.socket( socket.AF_INET , socket.SOCK_STREAM )
s.connect( ( host, port ) )

#########################################################################

start = time.process_time_ns()

try:
    for i in range(1,1000001): #10L        
        received_bytes = spi.readbytes(4)
        #print("receiving: {}".format(received_bytes))
        
        channel = received_bytes [0]
        data = received_bytes[1] << 16 | received_bytes[2] << 8 | received_bytes[3]
        #print("for channel: {}, data is: {}".format(channel,data))
        print_csv(channel, data )
        #print("\n")
        
        #try:
            #code for sending by socket here
        y = str( received_bytes )
        y = y.encode()
        s.send( y )
        
        #time.sleep(0.25)
       

except KeyboardInterrupt: # closes the function when Ctrl + C is pressed
    spi.close()
    s.close()

end = time.process_time_ns()
#end = time.time_ns()

print('time taken is: {}'.format( (end - start) ) )







