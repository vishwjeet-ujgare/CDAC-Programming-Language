program linkedin
    implicit none 
    

type node
    integer :: value
    type(node),pointer:: next=>null()
end type node

type(node)pointer :: head







! print*,"Head => ",head%value,"node1 => ",head%next%value

end program  linkedin