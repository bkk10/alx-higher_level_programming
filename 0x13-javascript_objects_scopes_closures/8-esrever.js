#!/usr/bin/node
exports.esrever = function (list){
	let reverselist = [];
	for (let i = list.length - 1; i >= 0; i--){
		reverselist.push(list[i]);
	}

	return reverselist;
}
