#!/bin/sh

../../bin/prms -C./control/sagehen.control
cp gmon.out ../../bin/gmon.out
cd ../../bin
gprof prms >> gprof_out.txt
