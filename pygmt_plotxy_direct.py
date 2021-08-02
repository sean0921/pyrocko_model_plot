#!/usr/bin/env python3

import pygmt
import pandas as pd
from sys import argv

depth = argv[1]

#ho1994xt_p.plot
p_xt = pd.read_csv(f'wu_2009_depth_{depth}_xt_p.plot',sep=' ',header=None,names=['time','distance'])
p_xt_mc = pd.read_csv(f'macintosh_2013test_depth_{depth}_xt_p.plot',sep=' ',header=None,names=['time','distance'])
#s_xt = pd.read_csv(f'wu_2009_depth_{depth}_xt_s.plot',sep=' ',header=None,names=['time','distance'])
p_xt_arrv = pd.read_csv(f'15260448.P20.plot',sep=' ',header=None,names=['time','distance'])
print(p_xt)
print(p_xt_arrv)

this_region = [ 
    0,  
    #s_xt.distance.max() + ( ( s_xt.distance.max() - s_xt.distance.min() ) * 0.4 ),
    p_xt_arrv.distance.max() + ( ( p_xt_arrv.distance.max() - p_xt_arrv.distance.min() ) * 0.4 ),
    0,  
    #s_xt.time.max(),
    p_xt_arrv.time.max(),
]

fig = pygmt.Figure()
fig.basemap(
        region=this_region,
        projection='X6.5i/6.5i',
        frame=['xa10+l"Distance(km)"','ya1+l"Time(s)"',f'WeSn+t"{depth} km Depth Time-Distance (Direct Wave)"']
)

fig.plot(x=p_xt.distance, y=p_xt.time, label=f"Wu(2009)" ,pen='0.05c,red')
fig.plot(x=p_xt_mc.distance, y=p_xt_mc.time, label=f"MacIntosh(2013)" ,pen='0.05c,purple')
#fig.plot(x=s_xt.time, y=s_xt.distance, label=f"s" ,pen='0.05c,red')
fig.plot(x=p_xt_arrv.distance, y=p_xt_arrv.time, style="c0.2c",pen='0.05c,blue')
fig.legend()

fig.savefig(f'pygmt_plotxy_direct_{depth}.png')
