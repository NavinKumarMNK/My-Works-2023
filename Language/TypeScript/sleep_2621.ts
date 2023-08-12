/*
const promise = new Promise<void>((resolve, reject) => {
    setTimeout(() => resolve(), 300);
    //setTimeout(() => reject(), 100) // Error
    
}) 

promise
    .then(() => console.log('resolved'))
    .catch(() => console.log('rejected'))
    .finally(() => console.log('done')) // done

*/

async function sleep(millis: number): Promise<void> {
    return new Promise<void>((resolve, reject) => {
        setTimeout(resolve, millis);
    });
}

let t = Date.now()
sleep(100).then(() => console.log(Date.now() - t)) // 100

async function hello() {
    await sleep(100);
    return 'hello';
}

async function helper() {
    const res = await hello();
    console.log(res);
}

helper(); // hello