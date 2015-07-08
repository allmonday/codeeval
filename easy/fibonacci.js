// todo use closure
function fibonacci(n) {
	if (n ===0 || n === 1) {
		return n;
	} else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
}

function memo(fn) {
	var cache = {};
	return function (n) {
		if( n in cache ) {
			return cache[n];
		} else {
			cache[n] = fn(n);
			return cache[n];
		}
	}
}

// mixed
var memoFibo = (function () {
	var cache = {};
	function f(n) {

		var val;

		if (n in cache) {
			val = cache[n];
		} else {
			if (n ===0 || n === 1) {
				val = n;
			} else {
				val = f(n-1) + f(n-2);
			}
			cache[n] = val;
		}
		return val;
	}	
	return f;
})()

console.log(fibonacci(5));

// little decorator
fibonacci = memo(fibonacci);
console.log(fibonacci(150));

// wrapper
console.log(memoFibo(145))

