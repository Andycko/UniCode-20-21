// This was my first solution which I attempted in JavaScript
// However, after I submited it I realized that I have rushed into this
// without thinking about it properly. It is a simple ROT-13 cipher, which means
// that all asci codes are shifted by 13.

halliday = function(message) {
    // Declare variables and the translation dictionary
    var decipheredMessage = "", wasUpper = false;
    const codes = {
        "a":"n",
        "b":"o",
        "c":"p",
        "d":"q",
        "e":"r",
        "f":"s",
        "g":"t",
        "h":"u",
        "i":"v",
        "j":"w",
        "k":"x",
        "l":"y",
        "m":"z",
        " ":" "
    };
    
    findValue = function(object, value) {
        // function to find a value in a dictionary and return it's key
        return Object.keys(object).find(key => object[key] === value)
    }
    
    for(var character of message) {
        // checking every character of the message and translating it with the 'codes' dictionary
        if (character == character.toUpperCase()){
            character = character.toLowerCase();
            wasUpper = true;
        }
        var newChar = codes[character];
        if (newChar) {
            if (wasUpper) newChar = newChar.toUpperCase();
            decipheredMessage += newChar;
        } else {
            newChar = findValue(codes, character);
            if (wasUpper) newChar = newChar.toUpperCase();
            decipheredMessage += newChar;
        }
        
        wasUpper = false;
    }
    return decipheredMessage;
};

console.log(halliday("Crystal Key"))