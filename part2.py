from astropy.io import fits
import numpy as np

with fits.open("discussion08_example.fits") as hdul:
    data = hdul[0].data

scaled_data = 10*data

hdu = fits.PrimaryHDU(scaled_data)
hdu.writeto("discussion08_scaled.fits", overwrite=True)
