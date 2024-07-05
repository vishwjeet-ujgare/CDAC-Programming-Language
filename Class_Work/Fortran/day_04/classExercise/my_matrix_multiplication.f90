program my_matrix_multiplication

    implicit none
    integer, allocatable,dimension(:,:) :: A,B,C

    integer :: i,j,done
    integer :: N=2

    real (kind=8):: start_time, end_time


    call cpu_time(start_time)
    !memory allocation 
    allocate(A(N,N),B(N,N),C(N,N))



    !inserting data to A, B
  
    do i=1,N 
        do j=1,N
            A(i,j)=1
            B(i,j)=1
        end do 
    end do

    C = A+B

    ! printing addition of A and B matrix
    print * ,"Matrix addition : "
       do i=1,N
        do j=1,N
            print * , C(i,j)
        end do 
    end do


  
  C = matmul(A,B)

    print * ,"Matrix Multiplication : "

  !printing matrix mulitplication 

     do i=1,N
        do j=1,N
            print * , C(i,j)
        end do 
    end do

! stat return 0 if succefull if not then -1

  deallocate(A,B,C, STAT=done)
  if(done /= 0) then
  	print *, "Could not release allocated arrays"
  	stop
  end if

call cpu_time(end_time)

print *, 'Execution time : ', end_time-start_time, ' seconds'

end program my_matrix_multiplication
