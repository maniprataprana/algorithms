// Generating all binary strings of n bits drawn  form 0...k-1


var nBitString = [];
function genrateString (n, k) {
	if (n < 1) {
		console.log(nBitString);
	} else {
		// use recursion to print all values
		for (var i = 0; i < k; i++) {
			nBitString[n-1] = i;
			genrateString(n-1, k);
		}

	}
}

genrateString(2);