// todo use closure
function fibonacci(n) {
	if (n === 1) {
		return 1;
	} else if (n === 0) {
		return 0;
	} else {
		return fibonacci(n-1) + fibonacci(n-2);
	}
}

function memoFibo(n) {
	var cache = {};
	if (cache[n]) {
		return cache[n];
	} else {
		cache[n] = fibonacci(n);
		return cache[n];
	}
}

console.log(fibonacci(5))
console.log(memoFibo(25))

