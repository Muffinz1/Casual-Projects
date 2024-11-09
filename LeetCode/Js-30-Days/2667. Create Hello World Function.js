/**
 * @return {Function}
 */
var createHelloWorld = function() {
    
    return function(...args) {
        const hello = "Hello World"
        return hello;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */