#!/usr/bin/env python3

import pygmt
import pandas as pd
pygmt.config(PS_MEDIA="A1")

#ps_vel = pd.read_csv(
#    '20220331_2017gc_2/vm_huang_2014_1d.txt',
#    #sep=' ', 
#    delim_whitespace=True,
#    index_col=False,
#    header=None,
#    names=['depth','P_velocity','S_velocity']
#)
#print(ps_vel)

a=pd.read_csv('00_adapted_model/macintosh-2013.test.m.nd',header=None,index_col=False,names=['depth','P_velocity','S_velocity','rho','qp','qs'],delim_whitespace=True)
ps_vel=a.drop(index=a[(a['depth']=='mantle')].index[0])
ps_vel['depth'] = pd.to_numeric(ps_vel['depth'])

this_region = [ 
    0,  
    ps_vel.P_velocity.max() + 3,
    0,  
    ps_vel.depth.max(),
]

fig = pygmt.Figure()
fig.basemap(
        region=this_region,
        projection='X6.5i/-6.5i',
        frame=['xa1f0.5+l"Velocity(km/s)"','ya5f1+l"Depth(km)"','WeSn+t"Velocity Model"']
)

fig.plot(x=ps_vel.P_velocity, y=ps_vel.depth, label=f"P-Velosity" ,pen='0.05c,blue')
fig.plot(x=ps_vel.S_velocity, y=ps_vel.depth, label=f"S-Velosity" ,pen='0.05c,red')
fig.legend()

fig.savefig('Model_3D_to_1D.png')
