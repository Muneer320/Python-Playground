import pyqrcode 

import png 

from pyqrcode import QRCode 

  

while True:  
	# String which represents the QR code 
	
	s = input("Please give the data to be given in the QR Code:\n")
	
	  
	# Generate QR code 
	
	url = pyqrcode.create(s) 
	  
	# Create and save the png file naming "myqr.png" 
	
	url.png('myqr.png', scale = 6) 
	
	print('Done')