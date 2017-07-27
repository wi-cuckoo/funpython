/***********************/
//	a simple and useful program
//	to check regular file between two line num
//	usage: he startline endline filename 
//	example: he 2 9 test.txt 
//	---- especially 'he 0 0 test.txt' to read whole file
//  2015/7/26 by louis wei
/***********************/

#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#define _GNU_SOURCE

int main (int argc, char *argv[])
{
//check if parameters is three
	if (argc != 4)
	{
		printf ("parameter error\n");
		return 1;
	}
//state start line and end line
	int staln = 0, endln = 0;
	staln = atoi (argv[1]);
	endln = atoi (argv[2]);

//accept parameter, no options	
//	char *filename;
//	filename = (char *)malloc(100); //this is critical
//	strncpy(filename, argv[3], sizeof(argv[3]-1));

//	printf("%s \n", filename);
//open the file into a stream	
	FILE *stream;
	stream = fopen (argv[3], "r");
	if (!stream)
	{
		perror ("open");
		return 1;
	}
//way 1 to read all file as reading one character each time
/*	
//	unsigned char c;  //if define c as unsigned char, mistake will occur
	int c;
	while((c = fgetc(stream)) != EOF)
	{
		++total_byte;
		printf("%c", (char)c);
	}
*/
//way 2 to read all file by fgets()
	char buffer[LINE_MAX];
	int ln = 0;
	int endless = 0;
	while (fgets(buffer, LINE_MAX, stream))
	{
		if (++ln >= staln && ln <= (endln == 0? ++endless: endln))
			printf ("%d	%s", ln, buffer);
		else if (ln > endln) 
			break;
		else
			continue;
	}
	
//	printf("\nthe total character is: %d\n", total_byte);

	if (fclose(stream) == EOF)
		perror ("close error");
//		fcloseall ();
	
	return 0;
}
