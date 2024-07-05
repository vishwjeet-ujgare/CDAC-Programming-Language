program students_record
  implicit none
  
  type students_data
  	integer::sub1,sub2,sub3,sub4
  	real::avg
  end type students_data
  
  type(students_data), allocatable, dimension(:):: myclass
  integer:: i, ok, done, class_size
  
  print *,"Input number of students in the class"
  read *, class_size
  
  allocate(myclass(class_size),STAT=ok)
  if(ok /= 0) then
  	print *, "Could not allocate arrays"
  	stop
  end if
  
  do i = 1, class_size
  	myclass(i)%sub1 = 10 + i
  	myclass(i)%sub2 = 20 + i
  	myclass(i)%sub3 = 30 + i
  	myclass(i)%sub4 = 40 + i
  end do
  
  !Calculate avg marks
  do i = 1, class_size
  	myclass(i)%avg = real(myclass(i)%sub1 + myclass(i)%sub2 + myclass(i)%sub3 + myclass(i)%sub4)/4.0;
  end do
  
  do i = 1,4
  	print *, 'myclass(i)%avg = ', myclass(i)%avg
  end do
  
  open(1,file='student.data')
  
  do i = 1, class_size
  	write(1,FMT=50)myclass(i)%sub1, myclass(i)%sub2, myclass(i)%sub3, myclass(i)%sub4
  end do
  
  50 FORMAT(4I5)
  
  close(1)
  
  deallocate(myclass, STAT=done)
  if(done /= 0) then
  	print *, "Could not release allocated arrays"
  	stop
  end if
end program students_record



