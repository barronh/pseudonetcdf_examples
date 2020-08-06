cmaq2cf
-------

author: Barron H. Henderson
date: 2020-08-06


Overview
========

This code shows how to add CF meta data using PseudoNetCDF. The CF meta data
is not the same as what can be added with IOAPI v3.2 (see below). However,
it may still be useful to users that do not have IOAPI.

From the perspective of this task, PseudoNetCDF is a meta-data aware wrapper
to netcdf4-python. So, it is essentially adding CF via python based on the
translation of IOAPI meta-data to CF metadata. The CF translation could be
improved, but works for many softwares.

Usage:

```
$ python cmaq2cf.py GRIDCRO2D.12US2.35L.160101 GRIDCRO2D.12US2.35L.160101.CF.nc
```

As of v3.2, IOAPI is capable of outputting CF metadata.[1] It is often not
done, but setting the `IOAPI_CFMETA` environmental variable to Y will add a
projection variable and coordinate variables. So, CMAQ can output files with
CF metadata. You can even add CF by extracting data from existing IOAPI files
to make copies with CF data.


[1] https://www.cmascenter.org/ioapi/documentation/all_versions/html/MODATTS3.html

