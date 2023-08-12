function createHelloWorld() {
	return (..._args: any):string=>'Hello World';
};

/**
 * function createHelloWorld() {
        return function(...args): string {
            return "Hello World";
        };
    };
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */

const f = createHelloWorld();
console.log(f()); // "Hello World"

// Clousure
/**
 * Creates a closure that returns an object with a function to increment a counter.
 * @returns An object with a function to increment a counter.
 */

function createCounter() {
    let counter = 0;

    function increment(){
        return ++counter;
    }

    return {
        increment: increment
    }
}

const counter1 = createCounter();
const counter2 = createCounter();

console.log(counter1.increment());
console.log(counter2.increment());
console.log(counter2.increment());


let a = [1, 2];
let b = [3, 4];

console.log([...a, ...b])

function add(...args: number[]) {
    console.log(args[0] + args[1]);
}

add(1, 2);