program area_reactangle
    implicit none
    
    !area is a funtion name and also 
    integer :: h, w, area,area1,perimeter

    h=10;
    w=20;

    area1=area(w,h)

    call calc_perimeter(w,h,perimeter)

    print*, "w :",w,"h =",h
    print* , "area = ",area1,"perimeter = ",perimeter
end program area_reactangle


function area (w,h)
    implicit none
    !to intent that we implicilty dont want to chagne w and h values

    !integer , intent(in) :: w,h
    ! are is not a dummy variabel int the sence it is not a argument 

!here we want to change w values implicitly but dont wan to chage h values and w and h are dummy values
    integer , intent(out) :: w
    integer , intent(in) :: h
    integer :: area
    w=5
    

    ! Dummy argument ‘w’ with INTENT(IN) in variable definition context
    !w=5
    !h=5

    area=w*h
    
end function area

subroutine calc_perimeter (w,h,perimeter)
    implicit none
    integer :: w, h , perimeter
    perimeter = 2 * (w+h)
end subroutine calc_perimeter


