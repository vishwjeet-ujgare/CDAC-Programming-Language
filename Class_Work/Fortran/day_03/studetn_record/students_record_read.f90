program students_record
  implicit none
  
  integer::sub1,sub2,sub3,sub4
  real::avg
  integer:: i, ios
 
  open(1,file='student.data')
  
  do 
  	read(1,FMT=50,IOSTAT=ios)sub1, sub2, sub3, sub4
  	if(ios < 0) exit
  	
  	avg = real(sub1 + sub2 + sub3 + sub4)/4.0;
  	print *, "avg = ", avg
  end do
  
  50 FORMAT(4I5)

  close(1)

end program students_record



