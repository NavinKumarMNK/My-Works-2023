/**
 * @param {Function} fn
 * @return {Function}
 */

function curry(fn: Function) : Function {
    let nums: any = [];
    
    return function curried(...args: any) : Function | number {
        nums = [...nums, ...args];
        
        if (fn.length === nums.length) {
            const res = fn(...nums);
            nums = [];
            return res;
        } else {
            return curried;
        }
    };

    /*
    return function curried(...args: any) : Function | number {
        if (args.length === fn.length) {
            return fn(...args);
        } else {
            return function(...args2: any) : Function | number {
                return curried(...args, ...args2);
            };
        }
    };
    */
};

// Test
function sum(a: number, b: number, c: number): number {
    return a + b + c;
}

const curriedSum = curry(sum);
console.log(curriedSum(1, 2, 3)); // 6
console.log(curriedSum(1)(2, 3)); // 6

