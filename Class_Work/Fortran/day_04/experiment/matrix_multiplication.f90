
program matrix_multiplication
  implicit none
  integer, allocatable, dimension(:,:) :: A, B, C
  integer :: i, j, width, ok, done
  
  print *,"Input width of the matrix"
  read *, width
  
  allocate(A(width,width),B(width,width),C(width,width),STAT=ok)
  if(ok /= 0) then
  	print *, "Could not allocate arrays"
  	stop
  end if
  
  do i = 1, width
     do j = 1, width
  	    A(i,j) = 1
  	    B(i,j) = 1
  	    C(i,j) = 1000
     enddo	
  enddo
  
  C = A + B
  
  print *, "Matrix Addition: "
  do i = 1, 4
     do j = 1, 4
  	    print *, C(i,j)
     enddo
  enddo
  
  
  C = matmul(A,B)
  
  print *, "Matrix Multiplication: "
  do i = 1, 4
     do j = 1, 4
  	    print *, C(i,j)
     enddo
  enddo
  
  deallocate(A,B,C, STAT=done)
  if(done /= 0) then
  	print *, "Could not release allocated arrays"
  	stop
  end if
end program matrix_multiplication


