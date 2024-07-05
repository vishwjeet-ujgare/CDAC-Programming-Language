
program vector_addition
  implicit none
  !integer, dimension(10000) :: A, B, C
  integer :: A(10000), B(10000), C(10000)
  integer ::i
  
  do i = 1, 10000
  	A(i) = i
  	B(i) = i
  	C(i) = 1000
  enddo
  
  do i = 1,10000 
  	C(i) = A(i) + B(i)             
  enddo

  !C = A + B	
  
  do i = 1,10
  	print *, C(i)
  enddo
  
end program vector_addition


