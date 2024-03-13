// Defanging an IP Address

//take a ip adresss from user {min IP is 0 and max ip is 255}
//store it in array
//then travel though a array and
//  if . is then go to for loop or while loop and then add to j [.] and if not then increment outer array 
//print new array

#include<stdio.h>
void main()
{

    printf("\n\nDefanging an IP Address\n\n");
    printf("Enter Appropriate IP addres that is each subset in 0-255 separated by dot only : ");
     
    char ip[15]="";
    int i=0;
    int ipLen=0;
    int j=0;
    char resIp[25]="";

    scanf("%15s",ip);

 printf("%s",ip);

while(ip[ipLen]!='\0')
{
    ipLen++;
}

for(;i<ipLen;i++,j++)
{
    
    if(ip[i]=='.')
    {
       
      resIp[j]='[';
      resIp[++j]='.';
      resIp[++j]=']';   
    }
    else
    {
        resIp[j]=ip[i];
      }

}

 printf("\n\n%s",resIp);
   
}