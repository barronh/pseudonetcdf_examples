import sys
import os
import PseudoNetCDF as pnc

# inpath = 'GRIDCRO2D.12US2.35L.160101'
# outpath = 'GRIDCRO2D.12US2.35L.160101.CF.nc'
try:
    inpath, outpath = sys.argv[1:]
except Exception as e:
    print('Usage: python {} <INPATH> <OUTPATH>'.format(sys.argv[0]))

if not os.path.exists(inpath):
    raise IOError(f'{inpath} does not exist.')

if os.path.exists(outpath):
    raise IOError(f'{outpath} exists. Will not overwrite.')

infile = pnc.pncopen(inpath, format='ioapi').copy()
pnc.conventions.ioapi.add_cf_from_ioapi(infile)
infile.save(outpath, verbose=0)
