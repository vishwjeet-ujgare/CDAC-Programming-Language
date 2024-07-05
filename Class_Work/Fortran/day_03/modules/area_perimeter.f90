module area_perimeter
implicit none
  integer:: width, height, area, perimeter
  contains 
	subroutine calc_for_rectangle()
	  implicit none
	  	print *,"Enter width and height of the rectangle"
	  	read *,width, height
		area = width*height
		perimeter = 2*(width+height)
	end subroutine calc_for_rectangle
	
	subroutine calc_for_square()
	  implicit none
	  	print *,"Enter width of the square"
	  	read *,width
		area = width*width
		perimeter = 4*width
	end subroutine calc_for_square
	
end module area_perimeter
