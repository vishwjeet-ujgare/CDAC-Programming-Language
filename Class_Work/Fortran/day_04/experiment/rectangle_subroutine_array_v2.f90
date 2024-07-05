
program rectangle
  implicit none
  
  integer, allocatable, dimension(:):: width, height, area, perimeter

  integer:: i, ok, done, arr_size
  
  interface
  	subroutine calc_values(width, height, area, perimeter)
 	  implicit none
	  integer, intent(in), dimension(:):: width, height
	  integer, intent(out), dimension(:):: area, perimeter
	end subroutine calc_values  
  end interface
  
  print *,"Input array_size"
  read *, arr_size
  
  allocate(width(arr_size),height(arr_size),area(arr_size),perimeter(arr_size),STAT=ok)

  if(ok /= 0) then
  	print *, "Could not allocate arrays"
  	stop
  end if
  
  do i = 1, arr_size
  	width(i) = i
  	height(i) = i
  end do
  
  call calc_values(width, height, area, perimeter)
  
  do i = 1,4
  	print *, 'area = ', area(i)," perimeter = ", perimeter(i)
  end do
  
  deallocate(width, height, area, perimeter)
  
end program rectangle


subroutine calc_values(width, height, area, perimeter)
 implicit none
	integer, intent(in), dimension(:):: width, height
	integer, intent(out), dimension(:):: area, perimeter
	integer:: i, arr_size

	arr_size = size(width)

	do i = 1, arr_size
		area(i) = width(i) * height(i)
  		perimeter(i) = 2 * (width(i) + height(i))
  	end do

end subroutine calc_values
