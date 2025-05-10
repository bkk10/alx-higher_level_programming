#!/usr/bin/node
const size = process.argv[2]
if (isNaN(size)){
	console.log("Missing size");
}
else{
	for (let row = 0; row < size; row++){
		let line = '';
		for (let col = 0; col < size; col++){
			line += '#';
		}
		console.log(line);
	}
}
