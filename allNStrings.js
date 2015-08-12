// Generating all binary strings of n bits


var nBitString = [];
function genrateString (n) {
	if (n < 1) {
		console.log(nBitString);
	} else {
		// use recursion to print all values
		nBitString[n-1] = 0;
		genrateString(n-1);
		nBitString[n-1] = 1;
		genrateString(n-1)
	}
}

genrateString(2);