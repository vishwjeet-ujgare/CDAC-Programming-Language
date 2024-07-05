program temp
        implicit none
        real :: tempC, tempF
! Convert 10C to farenheit
        tempF = 9.0 / 5.0 * 10.0 + 32.0
! Convert 40F to celsius
        tempC = 5.0 / 9.0 * (40.0 - 32.0 )
!        call display(tempC , tempF)

print *,'Temperature in celsius', tempC 
print *, 'Temperature in farenheit', tempF
end program temp
