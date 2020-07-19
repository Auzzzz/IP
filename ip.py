import math

## IP and Subnet mask ##

#IP to Binary takes the ip and returns the binary values
def iptobinary(ip):
  #Split ip into lists
  ip = ip.split(".")
  #convert each list element into binry
  binary = '{0:08b}.{1:08b}.{2:08b}.{3:08b}'.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
  
  return(binary)

def binarytoip(binary):
  
  binary = binary.split(".")
  ip = '{0}.{1}.{2}.{3}'.format(int(binary[0],2), int(binary[1],2), int(binary[2],2), int(binary[3],2))

  return ip

def prefix(mask):
  cidr = mask.count('1')
  return(cidr)
  
# Print values in list
print(iptobinary("192.168.0.1"))
mask = iptobinary("255.255.248.0")
print(prefix(mask))
print(binarytoip("11000000.10101000.00000000.00000001"))



## Network Adress ##
