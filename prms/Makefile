# prms makefile

include ../makelist

TARGET 	= $(BINDIR)/prms
LIBS	= $(LIBDIR)/libmmf.a

LIBOBJS = \
	call_modules.o \
	basin.o \
	climateflow.o \
	cascade.o \
	soltab.o \
	prms_time.o \
	obs.o \
	climate_hru.o \
	potet_jh.o \
	potet_pt.o \
	potet_hs.o \
	potet_pm.o \
	potet_pan.o \
	potet_hamon.o \
	ddsolrad.o \
	ccsolrad.o \
	ide_dist.o \
	xyz_dist.o \
	precip_1sta_laps.o \
	precip_dist2.o \
	temp_1sta_laps.o \
	temp_dist2.o \
	transp_frost.o \
	transp_tindex.o \
	frost_date.o \
	intcp.o \
	snowcomp.o \
	srunoff.o \
	soilzone.o \
	gwflow.o \
	water_balance.o \
	routing.o \
	strmflow.o \
	strmflow_in_out.o \
	muskingum.o \
	lake_route.o \
	strmflow_lake.o \
	subbasin.o \
	map_results.o \
	nhru_summary.o \
	write_climate_hru.o \
	prms_summary.o \
	basin_sum.o \
	utils_prms.o

####################################################
# Rules for targets
####################################################
$(TARGET): $(LIBOBJS) $(LIBS)
	$(RM) $(TARGET)
	$(ICC) $(LDFLAGS) -o $(TARGET) $(LIBOBJS) $(LIBS) $(FLIBS)

#
# Define all object files which make up the library
#


clean:
	$(RM) $(PRMSLIBTRUNK) $(TARGET)
	$(RM) *.o *.mod *~

call_modules.o: call_modules.f90
	$(IFC) -c $(IFFLAGS) call_modules.f90

basin_sum.o: basin_sum.f90 prms_module.mod prms_flowvars.mod prms_intcp.mod prms_snow.mod prms_srunoff.mod prms_gwflow.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod prms_obs.mod prms_muskingum.mod
	$(IFC) -c $(IFFLAGS) basin_sum.f90

subbasin.o: subbasin.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_set_time.mod prms_intcp.mod prms_srunoff.mod prms_soilzone.mod prms_gwflow.mod prms_lake_route.mod prms_snow.mod prms_climatevars.mod 
	$(IFC) -c $(IFFLAGS) subbasin.f90

ddsolrad.o: ddsolrad.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) ddsolrad.f90

ccsolrad.o: ccsolrad.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) ccsolrad.f90

snowcomp.o: snowcomp.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_climatevars.mod prms_set_time.mod prms_intcp.mod
	$(IFC) -c $(IFFLAGS) snowcomp.f90

gwflow.o: gwflow.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_intcp.mod prms_srunoff.mod prms_soilzone.mod prms_cascade.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) gwflow.f90

utils_prms.o: utils_prms.f90 prms_module.mod prms_basin.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) utils_prms.f90

prms_summary.o: prms_summary.f90 prms_module.mod prms_climatevars.mod prms_flowvars.mod prms_set_time.mod prms_obs.mod prms_intcp.mod prms_snow.mod prms_srunoff.mod prms_soilzone.mod prms_gwflow.mod
	$(IFC) -c $(IFFLAGS) prms_summary.f90

muskingum.o: muskingum.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_set_time.mod prms_obs.mod prms_srunoff.mod prms_gwflow.mod
	$(IFC) -c $(IFFLAGS) muskingum.f90

intcp.o: intcp.f90 prms_module.mod prms_basin.mod prms_obs.mod prms_climatevars.mod prms_flowvars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) intcp.f90

map_results.o: map_results.f90 prms_module.mod prms_basin.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) map_results.f90

nhru_summary.o: nhru_summary.f90 prms_module.mod prms_basin.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) nhru_summary.f90

soltab.o: soltab.f90 prms_module.mod prms_basin.mod
	$(IFC) -c $(IFFLAGS) soltab.f90

frost_date.o: frost_date.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) frost_date.f90

precip_1sta_laps.o: precip_1sta_laps.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) precip_1sta_laps.f90

transp_tindex.o: transp_tindex.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) transp_tindex.f90

transp_frost.o: transp_frost.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) transp_frost.f90

temp_1sta_laps.o: temp_1sta_laps.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) temp_1sta_laps.f90

temp_dist2.o: temp_dist2.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) temp_dist2.f90

precip_dist2.o: precip_dist2.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) precip_dist2.f90

strmflow.o: strmflow.f90 prms_module.mod prms_basin.mod prms_obs.mod prms_flowvars.mod prms_gwflow.mod prms_srunoff.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) strmflow.f90

strmflow_in_out.o: strmflow_in_out.f90 prms_module.mod prms_basin.mod prms_obs.mod prms_flowvars.mod prms_gwflow.mod prms_srunoff.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) strmflow_in_out.f90

potet_jh.o: potet_jh.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) potet_jh.f90

potet_pt.o: potet_pt.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod prms_climate_hru.mod
	$(IFC) -c $(IFFLAGS) potet_pt.f90

potet_hs.o: potet_hs.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) potet_hs.f90

potet_pm.o: potet_pm.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod prms_climate_hru.mod
	$(IFC) -c $(IFFLAGS) potet_pm.f90

potet_pan.o: potet_pan.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_obs.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) potet_pan.f90

potet_hamon.o: potet_hamon.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) potet_hamon.f90

write_climate_hru.o: write_climate_hru.f90  prms_module.mod prms_set_time.mod prms_climatevars.mod
	$(IFC) -c $(IFFLAGS) write_climate_hru.f90

climate_hru.o: climate_hru.f90 prms_module.mod prms_basin.mod prms_climatevars.mod prms_soltab.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) climate_hru.f90

cascade.o: cascade.f90 prms_module.mod prms_basin.mod
	$(IFC) -c $(IFFLAGS) cascade.f90

basin.o: basin.f90 prms_module.mod
	$(IFC) -c $(IFFLAGS) basin.f90

obs.o: obs.f90 prms_module.mod prms_set_time.mod prms_basin.mod
	$(IFC) -c $(IFFLAGS) obs.f90

srunoff.o: srunoff.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_climatevars.mod prms_cascade.mod prms_intcp.mod prms_snow.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) srunoff.f90

climateflow.o: climateflow.f90 prms_module.mod prms_basin.mod prms_set_time.mod
	$(IFC) -c $(IFFLAGS) climateflow.f90

soilzone.o: soilzone.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_snow.mod prms_climatevars.mod prms_cascade.mod prms_set_time.mod prms_intcp.mod prms_srunoff.mod
	$(IFC) -c $(IFFLAGS) soilzone.f90

routing.o: routing.f90 prms_module.mod prms_basin.mod prms_gwflow.mod prms_flowvars.mod prms_set_time.mod prms_srunoff.mod prms_climatevars.mod
	$(IFC) -c $(IFFLAGS) routing.f90

prms_time.o: prms_time.f90 prms_module.mod prms_basin.mod
	$(IFC) -c $(IFFLAGS) prms_time.f90

strmflow_lake.o: strmflow_lake.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_lake_route.mod prms_routing.mod prms_obs.mod prms_set_time.mod prms_srunoff.mod prms_gwflow.mod
	$(IFC) -c $(IFFLAGS) strmflow_lake.f90

lake_route.o: lake_route.f90 prms_module.mod prms_basin.mod prms_flowvars.mod prms_climatevars.mod prms_flowvars.mod prms_set_time.mod prms_srunoff.mod prms_soilzone.mod prms_gwflow.mod prms_obs.mod
	$(IFC) -c $(IFFLAGS) lake_route.f90

water_balance.o: water_balance.f90 prms_module.mod prms_basin.mod prms_srunoff.mod prms_flowvars.mod prms_gwflow.mod prms_climatevars.mod prms_set_time.mod prms_cascade.mod prms_intcp.mod prms_snow.mod prms_soilzone.mod
	$(IFC) -c $(IFFLAGS) water_balance.f90

prms_climatevars.mod: climateflow.o
prms_flowvars.mod: climateflow.o
prms_module.mod: call_modules.o
prms_gwflow.mod: gwflow.o
prms_obs.mod: obs.o
prms_basin.mod: basin.o
prms_soltab.mod: soltab.o
prms_intcp.mod: intcp.o
prms_snow.mod: snowcomp.o
prms_cascade.mod: cascade.o
prms_set_time.mod: prms_time.o
prms_soilzone: soilzone.o
prms_srunoff: srunoff.o
