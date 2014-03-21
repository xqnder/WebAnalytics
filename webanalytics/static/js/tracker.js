var startMilliseconds = (new Date).getTime();
// trackEnd runs when the user leaves the page:
window.onbeforeunload = trackEnd;

function trackEnd( event ) {

	var xhr = new XMLHttpRequest();

	var endMilliseconds = (new Date).getTime()

	// The data to send to the BE:
	var dataObject = {
		'origin': location.origin,
		'path': location.pathname,
		'duration': ( endMilliseconds - startMilliseconds ) / 1000
	};

	// URL encode it:
	var dataString = serialize( dataObject );

	xhr.open('GET', 'http://localhost:8000/visits?' + dataString, false);  // false means synchronous; waiting for response
	xhr.send();
}

function serialize( object ) {
	// Stackoverflow function which URL encodes a JS object so that we can put it in the GET request as arguments
	var str = [];
	for(var p in object)
	if (object.hasOwnProperty(p)) {
		str.push(encodeURIComponent(p) + "=" + encodeURIComponent(object[p]));
	}
	return str.join("&");
}