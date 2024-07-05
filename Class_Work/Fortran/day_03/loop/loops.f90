program loops
    implicit none
    
    integer :: i, n
    n=10

    print *,"Printing 1 - to 10"
    do i=1,n,1
        print *," i = ",i
    end do 

    print *,"================="
    print*,"do i=n,1,1 will print nothing"

    do i=n,1,1
        print *," i = ",i
    end do 

    print *,"================="
    print *,"Printing 10 - to 1"

    do i=n,1,-1
        print *," i = ",i
    end do 

    print *,"================="
    ! print *,"do i=n,1,-1 will print "

    ! do i=n,1,1
    !         print *," i = ",i
    !     end do 


end program loops
