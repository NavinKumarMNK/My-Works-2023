function createCounter(n: number): () => number {
    return function() {
        return n++;
    }
}

const counter = createCounter(10)
console.log(counter()) // 10
console.log(counter()) // 11
console.log(counter()) // 12

class Counter {
    n: number;
    constructor (public count: number = 0) {
        this.n = count;
    }

    increment() {
        return this.n++;
    }
}

const counter2 = new Counter(10);
console.log(counter2.increment()) // 10
console.log(counter2.increment()) // 11
console.log(counter2.increment()) // 12