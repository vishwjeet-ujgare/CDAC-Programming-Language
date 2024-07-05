.global _start
.section .data
	num1: .word 7
	num2: .word 9
	result: .word 0

.section .text 

_start:
	//loat the first number 7 into a register
	ldr x0,=num1

	//load the second number 9 into another register
	ldr x1,=num2

	//add the tow numbers together
	ldr w2,[x0] // load num1 into a 32 bit register
	ldr w3,[x1] //laoad  num2 into another 32-but register
	add  w4,w2,w3 //Add the two numbers

	//store the result back into memory
	ldr x5,=result
	str w4,[x5]

	//Exit the program
	mov x8, #92 //System call number for exit
	mov x0, #0 //Exist status
	svc #0	   //Invoke the system call

