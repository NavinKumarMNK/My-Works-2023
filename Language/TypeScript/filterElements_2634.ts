function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const res: number[] = [];
    for (const i in arr) {
        if (fn(arr[i], Number(i))) {
            res.push(arr[i]);
        } 
    }

    return res;
};