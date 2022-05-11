#!/usr/bin/env python3

import pygmt
import pandas as pd
from sys import argv

#model_type='macintosh_2013'
model_type='huang_2014'
#depth = '15.368'
depth = '15'
my_type = '.ew'

#ho1994xt_p.plot
p_xt = pd.read_csv(f'{model_type}_depth_{depth}_xt_p.plot',delim_whitespace=True, header=None,names=['time','distance'])
moho_xt = pd.read_csv(f'{model_type}_depth_{depth}_xt_moho.plot',delim_whitespace=True, header=None,names=['time','distance'])
#s_xt = pd.read_csv(f'{model_type}_depth_{depth}_xt_s.plot',delim_whitespace=True, header=None,names=['time','distance'])

p_xt_arrv_bg = pd.read_csv(f'15260448.P20.3.plot',delim_whitespace=True, header=None,names=['time','distance','sitename'])
pmp_xt_arrv_bg = pd.read_csv(f'pmp_like_arrival.3.plot',delim_whitespace=True, header=None,names=['time','distance','sitename'])
p_xt_arrv = pd.read_csv(f'15260448.P20.3{my_type}.plot',delim_whitespace=True, header=None,names=['time','distance','sitename'])
pmp_xt_arrv = pd.read_csv(f'pmp_like_arrival.3{my_type}.plot',delim_whitespace=True, header=None,names=['time','distance','sitename'])

this_region = [ 
    0,
    #s_xt.distance.max() + ( ( s_xt.distance.max() - s_xt.distance.min() ) * 0.4 ),
    #p_xt_arrv.distance.max() + ( ( p_xt_arrv.distance.max() - p_xt_arrv.distance.min() ) * 0.4 ),
    20,
    0,  
    #s_xt.time.max(),
    #p_xt_arrv.time.max(),
    8,
]

fig = pygmt.Figure()
fig.basemap(
    region=this_region,
    projection='X6.5i/6.5i',
    frame=['xa1+l"Distance(km)"','ya1+l"Time(s)"',f'WeSn']
)

fig.plot(x=p_xt.distance, y=p_xt.time, label=f"Direct" ,pen='0.05c,red')
fig.plot(x=moho_xt.distance, y=moho_xt.time, label=f"Reflection" ,pen='0.05c,purple')
##fig.plot(x=s_xt.time, y=s_xt.distance, label=f"s", pen='0.05c,red')

fig.plot(x=p_xt_arrv_bg.distance, y=p_xt_arrv_bg.time, style="c0.2c",pen='0.05c,grey')
fig.plot(x=p_xt_arrv.distance, y=p_xt_arrv.time, style="c0.2c",label=f"P_pick",pen='0.05c,blue')

fig.plot(x=pmp_xt_arrv_bg.distance, y=pmp_xt_arrv_bg.time, style="c0.2c",pen='0.05c,grey')
fig.plot(x=pmp_xt_arrv.distance, y=pmp_xt_arrv.time, style="c0.2c",label=f"PcP_pick",pen='0.05c,green')

###### '.ew'
p_xt_arrv_text = p_xt_arrv_bg.loc[[1,3,4,8,12,16,25,26,27],:]
fig.text(x=p_xt_arrv_text.distance, y=p_xt_arrv_text.time, text=p_xt_arrv_text.sitename.to_numpy(dtype='str'), offset='0.9/-1.5+v0.1',fill='white')
pmp_xt_arrv_text = pmp_xt_arrv_bg.loc[[0,4,7,14,15,16],:]
fig.text(x=pmp_xt_arrv_text.distance, y=pmp_xt_arrv_text.time, text=pmp_xt_arrv_text.sitename.to_numpy(dtype='str'), offset='-0.9/1.5+v0.1',fill='white')

#pmp_xt_arrv_text = pmp_xt_arrv.loc[[0,6],:]
#fig.text(x=pmp_xt_arrv_text.distance, y=pmp_xt_arrv_text.time, text=pmp_xt_arrv_text.sitename.to_numpy(dtype='str'), offset='-0.9/1.5+v0.1',fill='white')

fig.plot(x=[5.12,5.12], y=[1.65,2.5], color='black',pen='0.05c,black')
fig.plot(x=[10.1,10.1], y=[1.65,2.5], color='black',pen='0.05c,black')
fig.text(x=[7.6], y=[1.55], text=['Tainan Tableland'])

fig.legend()

fig.savefig(f'{model_type}_depth_{depth}_xt_0_20{my_type}.png')
