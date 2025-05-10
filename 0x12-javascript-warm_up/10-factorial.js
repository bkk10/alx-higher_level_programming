#!/usr/bin/node
const num = process.argv[2]
factorial = 1
if (isNaN(num)){
	console.log("1");
}
else{
	for (let i = 1; i <= num;i++){
		factorial *= i;
	}
	console.log(factorial);
}
