rm -rf *.o *.mod ./a.out
gfortran -c area_perimeter.f90
gfortran -c area_perimeter_module.f90
gfortran area_perimeter.o area_perimeter_module.o
