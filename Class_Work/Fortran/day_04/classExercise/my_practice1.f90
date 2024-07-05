program my_practice1
    implicit none

    integer,allocatable , dimension(:) :: a,aa

    integer :: i
    integer :: N=10

    real (kind=8) :: start_time, end_time


    call cpu_time(start_time)


    allocate(a(N),aa(N))

    !initializing vector

    do i=1,N 
        a(i)=i
    end do 


	! Add multiply two vectors
    do i =1,N 
        aa(i)=a(i)*a(i)
    end do 

    !printing the output 
    do i=1,N
        print * , aa(i)
    end do 

    call cpu_time(end_time)

    print *, 'Execution time : ', end_time-start_time, ' seconds'

end program my_practice1

