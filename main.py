### Author: Devin Whitten
### Main driver for normalization routine, intended for SEGUE medium-resolution spectra.

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import sys, os
sys.path.append("interface")
### Local
import norm_functions
from spectrum import Spectrum

from astropy.io import fits


files = os.listdir(os.getcwd() + "/Spectra/")

for filename in files:
    #filename = "spSpec-2371-53762-261.fit"
    input_file = fits.open("Spectra/" + filename)

    ### Create Spectrum object
    spec = Spectrum(input_file)

    ### generate segments
    spec.generate_segments()
    spec.assess_segment_variation()
    spec.define_cont_points()
    spec.spline_continuum()
    spec.normalize()

    norm_functions.plot(spec)
    output_file = norm_functions.update_fits(spec, input_file)
    output_file.writeto("output/" + filename.split(".")[0] + "_norm.fit")
