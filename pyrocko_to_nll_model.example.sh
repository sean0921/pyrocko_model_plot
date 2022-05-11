#!/bin/sh

grep -v 'mantle' 00_adapted_model/macintosh-2013.test.m.nd|awk '{printf "LAYER  %6.2f %6.3f  0.00 %6.3f  0.00 %6.3f  0.00\n",$1,$2,$3,$4}'
