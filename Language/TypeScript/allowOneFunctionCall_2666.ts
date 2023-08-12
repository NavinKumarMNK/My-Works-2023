type Fn = (...args: any[]) => any

function once(fn: Fn): Fn {
    let called = false;
    return function (...args) {
        if (called) {
            return undefined;
        } 
        called = true;
        return fn(...args);
    };
}

let fn = (a,b,c) => (a + b + c)
let onceFn = once(fn)

onceFn(1,2,3); // 6
onceFn(2,3,6); // returns undefined without calling fn
 

/*
const person = {
    name: 'John',
};

function sayHi(greeting1: string, greeting2: string) {
    console.log(`${greeting1} ${greeting2}, my name is ${this.name}`);
}

sayHi.apply(person, ['Hello', 'Good morning']); // Hello Good morning, my name is John
*/