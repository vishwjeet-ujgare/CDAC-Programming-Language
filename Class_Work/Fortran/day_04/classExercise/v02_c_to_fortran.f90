program pi
    implicit none
    
    real :: area, pie, dx, y, x
    integer :: i,j, N

    N = 999999
    dx = 1.0 / N
    x = 0.0
    area = 0.0

    do i=0, N, 1
        x = i*dx
        y = SQRT(1-x*x)
        area = area + y *dx
    end do

    pie = 4.0 * area
    print *, "Value of pi is = ", pie

end program pi