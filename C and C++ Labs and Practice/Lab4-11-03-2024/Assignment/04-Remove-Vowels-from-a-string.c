// Remove Vowels from a string

//1. take string from user
//2. find out legnth of a array
//3.travel though that string 
//4.and remove vowels in the sence add non vowel in another string


// -----------NOTE------------
// ifyou using scanf() to read input into array it is essential o allocate enough memory to prevent buffer overflow

#include<stdio.h>
void main()
{
    char str[100]="";
   
    int arrayLength=0;

    char resStr[100]="";
    int i =0;
    int j=0;

    printf("\n\nRemove Vowels from a string\n\n");
    printf("Enter a string : ");

    //limit  input to prevent buffer overflow so it will take max 9 character and onward 99 it will ignore
    //we dont use %9 then it will display error stack smahing detected
    scanf("%99s",str);


    while(str[arrayLength]!='\0')
    {
        arrayLength+=1;
        
    }
    printf("\n\nYour entered : %s",str);
    printf("\nLength enter string is : %d",arrayLength);


    for (i; i < arrayLength;i++)
    {

       if(str[i]=='a' || str[i]=='e'|| str[i]=='i'|| str[i]=='o'||str[i]=='u'||str[i]=='A' || str[i]=='E'||str[i]=='I'||str[i]=='O'||str[i]=='U')
       {
                        
       }
       else
       {

                    
            resStr[j]=str[i];
             j++;
       }
    }

 resStr[j]='\0';
     

 arrayLength=0;   
  while(resStr[arrayLength]!='\0')
    {
        arrayLength+=1;
       }   

    

     printf("\n\nResult String withoud vowel  : %s",resStr); 
     printf("\nLength of result string : %d\n",arrayLength);    
}