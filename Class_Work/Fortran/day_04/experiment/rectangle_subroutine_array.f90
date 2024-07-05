
program rectangle
  implicit none
  
  integer, allocatable, dimension(:):: width, height, area, perimeter
  integer:: i, ok, done, arr_size
  
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
  
  call calc_values(width, height, area, perimeter,arr_size)
  
  do i = 1,4
  	print *, 'area = ', area(i)," perimeter = ", perimeter(i)
  end do
  
  deallocate(width, height, area, perimeter,STAT=done
  )
  if(done /= 0) then
  	print *, "Could not release allocated arrays"
  	stop
  end if
end program rectangle


subroutine calc_values(width, height, area, perimeter,arr_size)
 implicit none
	integer, intent(in), dimension(arr_size):: width, height
	integer, intent(out), dimension(arr_size):: area, perimeter
	integer:: i

	integer, intent(in)::arr_size
	do i = 1, arr_size
		area(i) = width(i) * height(i)
  		perimeter(i) = 2 * (width(i) + height(i))
  	end do

end subroutine calc_values
