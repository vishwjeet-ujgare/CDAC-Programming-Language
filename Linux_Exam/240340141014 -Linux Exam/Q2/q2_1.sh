#!/bin/bash

#taking inpusts for user1 
echo "Enter name of user 1:"
read u1_name

echo "Enter city of user 1:"
read u1_city

echo "Enter age of user 1:"
read u1_age

#taking input  for user2
echo"========================="

echo "Enter name of user 2:"
read u2_name

echo "Enter city of user 2:"
read u2_city

echo "Enter age of user 2:"
read u2_age


# Compare city is same or not 
if [ "$u1_city" = "$u2_city" ]; then
    echo "Lets meet and greet, we belong to the same city."
else
    echo "Lets schedule a virtual meeting to know more about each other."
fi


#comparing age if {[an to it i elif statement as well]}

ageDiff=$((u1_age - u2_age))

#reseting agedDiff if gone into minus
if [ $ageDiff -lt 0 ]; then
	ageDiff=$((u2_age - u1_age))
fi



#now comparing age and printing msg 
if [ $ageDiff -gt 1 ] && [ $ageDiff -lt 4 ]; then
    echo "Hello Mate !! It seems we belong to same generation."
elif [ $ageDiff -gt 4 ]; then
    echo "Hello Mate, what's new going on in your age group?"
fi


