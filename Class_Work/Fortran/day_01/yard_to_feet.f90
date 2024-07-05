program yard_feet
implicit none
integer :: yard, feet, inch
print *, "enter yard : "
read *,yard
feet = 3 * yard
inch = 12 * feet
print *, "feet = ", feet ,"inches = ", inch
end program yard_feet