void main()
{
     char bufferA[50];
     char bufferB[16];

     printf("what is your name?\n");

     gets(bufferA);

     strcpy(bufferB, bufferA);
     return; 
}

