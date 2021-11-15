pseudonetcdf examples
=====================

A repository of pseudonetcdf examples. These examples are designed to do basic tasks associated with Air Quality models. Each example was working when it was posted and can be run in the cloud. This allows users to test processing examples without their own computational environment. The same examples can also be run on your own Windows, Linux, or Mac environment.

Some examples use data from the web that may have moved. If you find an example that does not work, [open an issue](https://github.com/barronh/pseudonetcdf_examples/issues). Also, feel free to propose a fix.


Current Examples:

* Convert CMAQ NetCDF files to:
  * `cmaq2cf` - Climate Forecasting NetCDF files.
  * `cmaq2wrf` - WRF meta data NetCDF files.
* `cmaq_ozone_evaluation` - Evaluate CMAQ against ozone from AQS.
* `cmaq_mask_maker` - Make masks (fractional grid-cell) based on shapefiles
* Process Emissions Files
  * `csv2camxemis` - Convert CSV files to CAMx v6 emissions.
  * `cmaq_emis_profile` - add vertical allocation to CMAQ emissions.
* `prepcolab` - Prepares Google Colaboratory to use PseudoNetCDF.
* `example` - An example of how to make an example.

Live Testing
------------

To open any of these live, you have options: 

* [open this repo in colab](https://colab.research.google.com/github/barronh/pseudonetcdf_examples) and select the notebook you want to run.
* [open this repo in binder](https://mybinder.org/v2/gh/barronh/pseudonetcdf_examples/HEAD)


Please add/propose your own examples!
-------------------------------------

* See `example` for instructions and as a template.
* If you have a need for an example, feel free to [open an issue where you propose it](https://github.com/barronh/pseudonetcdf_examples/issues).
