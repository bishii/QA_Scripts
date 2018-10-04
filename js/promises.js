


var delays = new Promise(
	function(resolve,reject) {
		resolve(hold(5000));

		if (1 == 0){
			reject("error!")
		}

	}
	);

function hold(seconds) {
	setTimeout( function() {
		console.log( 'Dude, hold on for a minute!' );
		}, seconds);
	return seconds - 1000;
}

var result = function() {
	delays
	.then(success => {
		resultA = success;
		return resultA;
	})

	.then(success => hold(success))

	.then(success => {
		resultB = success;
		return resultB;
	})

	.then(success => hold(success))

	.then(success => {
		resultC = success;
		return resultC;
	})

	.then(success => {
		console.log('total: ' + success)
		console.log(resultA, resultB, resultC)
	})
}

result();