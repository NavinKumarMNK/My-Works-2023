type F = (x: number) => number;

function compose(functions: F[]): F {
	return function(x) {
        for (const fn of functions.reverse()) {
            x = fn(x);
        }

        return x;
    }
};

const fn = compose([x => x + 1, x => 2 * x])
fn(4) // 9


/**
type F = (x: number) => number;

function compose(functions: F[]): F {
	const fn = (acc: number, f: F) => f(acc);
    return function(x) {
        return functions.reduceRight(fn, x);
    };
};

 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */