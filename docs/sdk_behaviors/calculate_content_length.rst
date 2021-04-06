.. _sdk-calculate-content-length:

Request body content length
~~~~~~~~
By default, any requests that takes in an optional content length in the SDK will try calculate body's content length if the content length is not provided. 
If the request body contains a string, then content length will calculated by giving the length of the string.
If the request body is a stream, the SDK will check to see if the request stream body contains a tell and seek property to calculate content length and reset the stream's cursor back to its original position.
If the stream is not resetable, the stream will be buffered into memory at a rate of 128MB per read action to calculate the content length. A buffer_limit may be passed into the request to provide a buffer limit.
The stream will be read until the buffer is at its limit. If so, it will throw an exception to tell customer to pass in the content-length of the file instead.
If the buffer_limit is not passed in, then the buffer_limit will be defaulted to 100MB.. Note that for big streams, there is a chance there will be a write timeout.
One way to get around this is to increase the timeout, turn off the timeout when creating a service client or to pass in the content-length in the request.
Customers may experience slow performance for calculating content length on a large file. If the file is very large, it may freeze the process. Consider passing in content-length for big files.
If content length is not provided and the SDK is unable to calculate the content length of the request body, then an exception will be thrown to tell the user to pass in the content length to the request.
If the content length is already provided in the request, then the SDK will use the content length provided in the request.