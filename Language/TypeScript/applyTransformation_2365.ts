function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const res: number[] = [];
    for (const i in arr) {
        res.push(fn(arr[i], Number(i)));
    }
    return res;
};