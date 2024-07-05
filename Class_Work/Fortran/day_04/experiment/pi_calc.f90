
program pi_calc
implicit none
  integer(kind=8) :: N
  integer(kind=8) :: i
  real (kind=8) :: x, y, area, dx, tmp_y
  real (kind=8) :: start_time, end_time
  
  N = 999999999
  dx = 1.0d0/real(N)
  x = 0.0d0
  area = 0.0d0

  call cpu_time(start_time)
  
  !omp parallel do default(none) private(x,y) shared(dx) reduction(+:area) 
  do i = 1, N
    x = i*dx
    y = sqrt(1.0 - x*x)
    area = area + y*dx
  end do
  !omp end parallel do
  
  call cpu_time(end_time)
  
  area = area * 4
  
  print *, 'Value of pi is : ', area
  print *, 'Execution time : ', end_time-start_time, ' seconds' 
  
end program pi_calc
