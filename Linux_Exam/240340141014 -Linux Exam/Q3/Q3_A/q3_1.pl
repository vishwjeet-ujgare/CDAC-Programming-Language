
#
#write a PERL script to solve the below problme statemet , each solution must be developed using subroutiness
#1) write a script to check whether string is palindrom or not ?
#sample input :
#        lebel : it is a palindorme string
#        label : it is not a palindorm string
#subrouting is a funtion '



#!/usr/bin/perl
use strict;
use warnings;

#to use a strict mode
#created a funtion to check whether string is palindrome or not 
sub is_palindrome {
   
    #storing first parameter to word which is passed during function call
    my $word = shift;
    
    #splited word and store it in to array called letter 
    my @letters = split(//, $word);

    #scaler will give you a length of array.
    my $length = scalar @letters;

    #storing default value for variable 1 that is true
    my $is_palindrome = 1;


    #looping till the half of the length .. range 0 to half length of array
    for my $i (0 .. $length / 2) {
    
	    #checking last and first element and if it is not equal go inside if and 
	     if ($letters[$i] ne $letters[$length - $i - 1]) {
       	  
            #then make above variabe to false that is 0
            $is_palindrome = 0;
           
	    #break
	    last;
        }
    }

    #return true or false that 1 or 0
    return $is_palindrome;
}


#start point of the programe
print "Enter a word: ";

#taking input from usre and storing it into word
my $word = <STDIN>;

#chomp for removing new line charatcter at the end of input 
chomp $word;


#calling function with string word
if (is_palindrome($word)) {
    print "$word is a palindrome.\n";
} else {
    print "$word is not a palindrome.\n";
}

