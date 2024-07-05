program pointerExample
implicit none

   integer, pointer :: p1
   integer, target :: t1 
   integer, target :: t2
   
   p1=>t1
   p1 = 1
   
   Print *, p1
   Print *, t1
   
   p1 = p1 + 4
   Print *, p1
   Print *, t1
   
   t1 = 8
   Print *, p1
   Print *, t1
   
   nullify(p1)
   Print *, t1
   Print *, associated(p1)
   
   !t2 = 100
   
   p1=>t2
   Print *, associated(p1)
   Print*, associated(p1, t1)
   Print*, associated(p1, t2)
   
   !what is the value of p1 at present
   Print *, p1
   Print *, t2
   
   p1 = 10
   Print *, p1
   Print *, t2
   
end program pointerExample
