// this is a file operation exercise
// 2015/7/24
// for personal learning
//	
//


#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<stdio.h>
#include<unistd.h>
#include<string.h>
//#include<getopt.h>  //for supporting long option looks like --help
#include<errno.h>

void dof_read( int _fd)
{
	ssize_t ret;
	int total_byte = 0;
	char buf[1025];
	while((ret = read(_fd, buf,1024)) > 0)
	{
		if(ret == -1)
		{
			if(errno == EINTR)
				continue;
			perror("read failed");
			break;
		}
		total_byte += ret;
		printf("%s", buf);
		memset(buf, 0, 1024);      //this is a important operation to blush buf
	}
	printf("\nthe total bytes is: %d \n", total_byte);

}

void dof_write(int _fd)
{
	const char *buf = "fuck the programming\n";
	ssize_t nr;

	nr = write(_fd, buf,strlen(buf));
	if(nr == -1)
	// error 
	{
		perror("write failed");
	}

}
int main(int argc, char *argv[])
{

	char *filename;
	char flag;
//get parameters from terminal
	int ch;
	opterr = 0;
	while((ch = getopt(argc, argv, "c:s:w:h")) != -1)
	{
		switch(ch)
		{
			case 'c': 
				flag = 'c';
				strcpy(filename, optarg);
			   	break;
			case 's': 
				flag = 's';
			   	strcpy(filename, optarg);
			   	break;
			case 'w':
			   	flag = 'w';
			   	strcpy(filename, optarg);
			   	break;
//			case 'h': flag = 'h'; break;
//			default :; 
		}
	}

// to get non-optional parameter
	if(argv[optind] != NULL)
		strncpy(filename, argv[optind], sizeof(argv[optind])-1);

	printf("%s\n",filename);
//	open a file, if no exist, creat it
	int fd;
	fd = open(filename, O_RDWR|O_CREAT|O_NONBLOCK, 0644);
	if(fd == -1)
	{
		//error info ouput
		perror("wtf");
		return 1;
	};

//read a file
	if(flag == 's')
		dof_read(fd);
//write to a file
	
	fdatasync(fd);

	if(close(fd) == -1)
		perror("close");
	
	return 0;
}

