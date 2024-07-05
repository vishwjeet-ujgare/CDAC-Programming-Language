program practice2
    implicit none
    
    integer :: size=10
    integer :: i =0;
    
    real , allocatable , dimension(:) :: a , b, c 
    real :: alpha=0.001
    real (kind =8)=start_time, end_time

    call cpu_time(start_time)

    allocate(a(size),b(size),c(size))

!Assigning values
    do  i=1,size
        a(i)=i
        b(i)=i
        c(i)=0
    end do 

!doing calculatiion and storing result into c 
    do i =1,size   
        c(i)=a(i)+(alpha*b(i))
    end do 


!priting c

do i=1,size
    print * , c(i)
end do 


call cpu_time(end_time)
  

print * , ""



end program practice2