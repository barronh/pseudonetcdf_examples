Vertically Allocate Emissions with PseudoNetCDF
===============================================

author: Barron H. Henderson
date: 2020-08-20


Overview
--------

This example shows how to vertically allocate 2-d emissions using a known
layer fraction. It uses a publicly available emission file and an arbitrary
profile (44 layers like H-CMAQ). Better profiles can be found in the
literature[1-3], but would need to be converted to CMAQ layer structure.

[Open Live In Colab](https://colab.research.google.com/github/barronh/pseudonetcdf_examples/blob/main/cmaq_emis_profile/cmaq_emis_profile.ipynb)

References
----------

[1] Bieser, J., Aulinger, A., Matthias, V., Quante, M., Denier van der Gon, H.A.C., 2011. Vertical emission profiles for Europe based on plume rise calculations. Environmental Pollution 159, 2935-2946. https://doi.org/10.1016/j.envpol.2011.04.030

[2] Simpson, D., Benedictow, A., Berge, H., Bergström, R., Emberson, L. D., Fagerli, H., Flechard, C. R., Hayman, G. D., Gauss, M., Jonson, J. E., Jenkin, M. E., Nyíri, A., Richter, C., Semeena, V. S., Tsyro, S., Tuovinen, J.-P., Valdebenito, A., and Wind, P.: The EMEP MSC-W chemical transport model - technical description, Atmos. Chem. Phys., 12, 7825-7865, https://doi.org/10.5194/acp-12-7825-2012, 2012.

[3] Publicly available EMEP r4-34 input. EmisHeights.txt in ftp://ftp.met.no/projects/emep/OpenSource/202001/input_data/other_input_files.tar.bz2
