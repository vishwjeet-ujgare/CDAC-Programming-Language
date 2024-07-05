program calc_values
  use area_perimeter, only: area, perimeter, calc_for_rectangle, calc_for_square
  implicit none
  
  integer:: geometry_type
  
  print *, "Enter Geometry type (1:rectangle, 2:square)"
  read *, geometry_type
  
  if((geometry_type>2).or.(geometry_type<1))then
  	print *,'Invalid input. Exitting...'
  	call exit(0)
  end if
  
  
  select case(geometry_type)
  	case(1)
  		call calc_for_rectangle()
  	case(2) 
  		call calc_for_square()	
  end select	
  
  print *, 'area = ', area," perimeter = ", perimeter
  
end program calc_values

