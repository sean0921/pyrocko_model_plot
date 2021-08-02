#!/usr/bin/env python3

import pygmt
import pandas as pd
from sys import argv

depth = '15.368'
my_type = '29_35'

#ho1994xt_p.plot
p_xt = pd.read_csv(f'macintosh_2013_depth_{depth}_xt_p.plot',sep=' ',header=None,names=['time','distance'])
moho_xt = pd.read_csv(f'macintosh_2013_depth_{depth}_xt_moho.plot',sep=' ',header=None,names=['time','distance'])
#s_xt = pd.read_csv(f'macintosh_2013_depth_{depth}_xt_s.plot',sep=' ',header=None,names=['time','distance'])
p_xt_arrv = pd.read_csv(f'15260448.P20_tn_{my_type}.plot',sep=' ',header=None,names=['time','distance','sitename'])
pmp_xt_arrv = pd.read_csv(f'pmp_like_arrival_{my_type}.plot',sep=' ',header=None,names=['time','distance','sitename'])
print(p_xt)
print(p_xt_arrv)
print(pmp_xt_arrv)

this_region = [ 
    0,
    #s_xt.distance.max() + ( ( s_xt.distance.max() - s_xt.distance.min() ) * 0.4 ),
    #p_xt_arrv.distance.max() + ( ( p_xt_arrv.distance.max() - p_xt_arrv.distance.min() ) * 0.4 ),
    20,
    0,  
    #s_xt.time.max(),
    #p_xt_arrv.time.max(),
    7,
]

fig = pygmt.Figure()
fig.basemap(
        region=this_region,
        projection='X6.5i/6.5i',
        frame=['xa1+l"Distance(km)"','ya1+l"Time(s)"',f'WeSn+t"{depth} km Depth Time-Distance curve by Wu(2009)"']
)

fig.plot(x=p_xt.distance, y=p_xt.time, label=f"Direct" ,pen='0.05c,red')
fig.plot(x=moho_xt.distance, y=moho_xt.time, label=f"Moho" ,pen='0.05c,purple')
#fig.plot(x=s_xt.time, y=s_xt.distance, label=f"s" ,pen='0.05c,red')
fig.plot(x=p_xt_arrv.distance, y=p_xt_arrv.time, style="c0.2c",label=f"P_pick",pen='0.05c,blue')
fig.text(x=p_xt_arrv.distance, y=p_xt_arrv.time, text=p_xt_arrv.sitename.to_numpy(dtype='str'), offset='0.5/0.5+v0.1')
fig.plot(x=pmp_xt_arrv.distance, y=pmp_xt_arrv.time, style="c0.2c",label=f"PmP_pick",pen='0.05c,green')
fig.text(x=pmp_xt_arrv.distance, y=pmp_xt_arrv.time, text=pmp_xt_arrv.sitename.to_numpy(dtype='str'), offset='0.5/0.5+v0.1')
fig.legend()

fig.savefig(f'macintosh_2013a_depth_{depth}_xt_0_20_{my_type}.png')
