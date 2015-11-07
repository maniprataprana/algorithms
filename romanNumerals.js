function convert(num) {
 	var roman ="";

 	var symbols = {
 		1000:"M",
 		900:"CM",
 		500:"D",
 		400:"CD",
 		100:"C",
 		90:"XC",
 		50:"L",
 		40:"XL",
 		10:"X",
 		9:"IX",
 		5:"V",
 		4:"IV",
 		1:"I"
 	}

 	while(num >= 1000) {
 		roman += symbols[1000];
 		num -= 1000;
 	}

 	while(num >= 900) {
 		roman += symbols[900];
 		num -= 900;
 	}

 	while(num >= 500) {
 		roman += symbols[500];
 		num -= 500;
 	}

 	while(num >= 400) {
 		roman += symbols[400];
 		num -= 400;
 	}
 	while(num >= 100) {
 		roman += symbols[100];
 		num -= 100;
 	}
 	while(num >= 90) {
 		roman += symbols[90];
 		num -= 90;
 	}
 	while(num >= 50) {
 		roman += symbols[50];
 		num -= 50;
 	}
 	while(num >= 40) {
 		roman += symbols[40];
 		num -= 40;
 	}
 	while(num >= 10) {
 		roman += symbols[10];
 		num -= 10;
 	}
 	while(num >= 9) {
 		roman += symbols[9];
 		num -= 9;
 	}

 	while(num >= 5) {
 		roman += symbols[5];
 		num -= 5;
 	}
 	while(num >= 4) {
 		roman += symbols[4];
 		num -= 4;
 	}
 	while(num >= 1) {
 		roman += symbols[1];
 		num -= 1;
 	}
 	return roman;
}

convert(3600);
