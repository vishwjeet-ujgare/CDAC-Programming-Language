program area_of_cylinder
    implicit none

    real ::r,h ,pi,area_from_func1,area_from_func,area_from_subrn

    r=5
    h=5
    pi=3.14

    area_from_func1=area_from_func(pi, r, h)
    call area_from_subroutine(pi, r, h,area_from_subrn)

    print* ,"Cylinder height : ",h,"width : ",r ,"Pi : ",pi

    print*, "Area of Cylinder from function : ",area_from_func1
    print*, "Area of Cylinder from subroutine : ",area_from_subrn


end program area_of_cylinder


function area_from_func(pi, r, h)
    implicit none
    real ,intent(in)::pi,r,h
    real :: area_from_func

    area_from_func=(2*pi*r*h)+(2*pi*r*r)
    
end function area_from_func


subroutine area_from_subrn(pi, r, h,area_from_subrn)
    implicit none
    real ,intent(in)::pi,r,h,area_from_subrn

    area_from_subrn=(2*pi*r*h)+(2*pi*r*r)
end subroutine area_from_subrn