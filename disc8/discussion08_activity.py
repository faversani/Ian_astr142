import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

# Image size
width, height = 512, 512

# Create a meshgrid of x and y values
x = np.linspace(0, 4*np.pi, width)  
y = np.linspace(0, 4*np.pi, height) 
X, Y = np.meshgrid(x, y)

# Create sinusoidal wave interference pattern
Z = np.sin(X) + np.sin(Y)

# Normalize
Z_normalized = ((Z - Z.min()) / (Z.max() - Z.min()))

# Display the image
plt.imshow(Z_normalized, cmap='gray', origin='upper')
plt.colorbar()
plt.title('2D Interference Pattern')
plt.show()

#create 2d gaussian

gauss1d = np.random.normal(size = 10000)
gauss2nd = np.random.normal(size = 10000)


print(gauss1d.size)

plt.scatter(gauss1d, gauss2nd)
plt.show()


# save the data into a fits file

hdr = fits.Header()
hdr['DATE'] = '23-10-25'
hdr['AUTHOR'] = "Ian Faversani"
primary_hdu = fits.PrimaryHDU(data=Z_normalized, header = hdr)
image_hdu = fits.ImageHDU(data=[gauss1d, gauss2nd], name="2d gaussian", header=hdr)
hdul = fits.HDUList([primary_hdu, image_hdu])

output_filename = 'disc8.fits'
hdul.writeto(output_filename, overwrite=True)
     

    
    


