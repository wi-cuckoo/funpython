# System Programming 
=========================================
## Buffer I/O
----------------
**To study C, you should be well aware of low-level of system**
### User Space
Differ with those system callers like `open(0`, `read()`, etc, *stream* is 
in user space, not kernel space. So it can be read and write more fastly.

`\#include <stdio.h>` is the main header file. 

#### int fileno (FILE *stream) ####
On success, `fileno()` returns the file descriptor associated with `stream`.Programmers must exercise caution intermixing standard I/O calls with system calls. Before you manipulate the backing fd, you\'d better flush the stream by `fflush()`.

#### buffer type and control ####
`int setvbuf (FILE *stream, char *buf, int mode, size_t size)` to set the buffer type of stream to mode, as mode to be defined by following </br>
> - _IONBF    Unbuffered
> - _IOLBF	Line-buffered
> - _IOFBF	Block-buffered
</br>
warning: setvbuf() should be called after opening the stream but before any other operations.

## Advanced I/O ##
------------------------
### Scatter/Gather I/O ###
The standard read and write system calls provide *linear I/O*, scatter/gather I/O provides several advantages over linear I/O methods.
#### readv() and writev() ####
They\'re system calls. the readv() reads count segments from the fd into bufdescribed by `iov`, and writev() do the writing operation.
<pre> 
 struct iovec {
		void *iov_base; /* pointer to start of buffer */
		size_t iov_len; /* size of buffer in bytes */
	};
</pre>
each ivoec structure describes an independent disjoint buffer, which is called *segment*, and a set of segments is called a *vector*. In fact, all I/O inside the Linux Kernel is vectored; read() and write() are implemented ad vectored I/O with a vector of only one segment.

#### epoll() ####

Epoll decouples the monitor registration from the actual monitoring.

An epoll context is create via epoll_create1();

	int epoll_create1(int flags);

flags only can be chosed as EPOLL_CLOEXEC. It enables close-on-exec behavior.

#### Edge- Versus Level-Triggered Events

Wirh a level-tiggered watch, the call to epoll_wait() will return immediately, showing that the pipe is ready to read. With an edge-triggered watch, even if the pipe is readable at the invocation of epoll_wait(), the call will not reaturn until the data is written onto the pipe.

