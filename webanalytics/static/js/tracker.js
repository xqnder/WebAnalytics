if (document.readyState === 'complete' || document.readyState === 'loaded') {
	track();
}
else {
	document.addEventListener('DOMContentLoaded', track );
}

function track( event ) {

	console.log( event );
	var xhr = new XMLHttpRequest();
	// Before making the actual request, you should define a handler function that will be called in response to various events. This handler will be called once for each of the four cases:

	xhr.onreadystatechange = function() {
	   if (xhr.readyState == 1) {
	      console.log('The call to open(...) succeeded.');
	   }
	   if (xhr.readyState == 2) {
	      console.log('The call to send(...) succeeded.  Waiting for response...');
	   }
	   if (xhr.readyState == 3) {
	      console.log('The response is coming in!');
	   }
	   if (xhr.readyState == 4) {
	      console.log('We now have the complete response: ' + xhr.response);
	   }
	};

	//Now we can actually make the request:

//	xhr.open('POST', 'localhost:8000/visits', true);
//	var params = "param1=localhost:8000/test_counting";
//	xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
//	xhr.send(params);

	var dataString = 'localhost:8000/test_counting';
	xhr.open('GET', 'http://localhost:8000/visits?visit=' + dataString, true);
	xhr.send();

	//Here, the true argument means asynchronous. We could set this to false, and then the call would block until the request is received. Also, GET is the HTTP verb. You can also make POST requests (or any other type of request). If you were making a POST call, you might also want to pass data to the call to send, rather than the empty string.

	// Alternatively, using jQuery, we can write this entire request as long jQuery is being included in the head of the document:

	//$.ajax({
	//   url:’/url/to/something’,
	//   success:function(data){
	//      console.log('We now have the complete response: ' + data);
	//   }
	//});

	// It should be noted that unless jQuery is already being used, this might be wasteful as it means downloading all of jQuery just to register the page visit.
}