program cToFortran
    implicit none

    integer :: i,j
    integer:: N=999999
    real :: dx,y,x,area,pi

    dx=1.0/N
    
    x=0.0
    
    area=0.0

    do i=0,N
        x=i*dx
        y=SQRT(1-x*x)
        area=area + y * dx
    end do

    pi = 4.0 * area
    print * ,"Value of pi is = ",pi
end program cToFortran
        