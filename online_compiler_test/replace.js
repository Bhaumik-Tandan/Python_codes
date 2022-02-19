var {readFile,writeFile} = require('fs');

async function runner(functionName, input, expected) {
    return readFile(`test.py`, 'utf8', function(err, data) {
        if (err) throw err;
        data=`from ${functionName} import *\n${data}\ntest(${functionName},[${input}],[${expected}])`;
        writeFile(`result.py`, data, 'utf8', function(err) {
            if (err) throw err;
        });

});
}

runner("fib",[0,1,-1,-2,5], [0,1,-1,-2,3]);