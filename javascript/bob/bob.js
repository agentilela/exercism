//
// This is only a SKELETON file for the "Bob" exercise. It's been provided as a
// convenience to get you started writing code faster.
//

var Bob = function() {};

Bob.prototype.hey = function(input) {
  if (input === input.toUpperCase() && input.match(/[a-z]/i)) {
    return "Whoa, chill out!";
  }
  
  if (input[input.length - 1] === "?") {
    return "Sure.";
  }

  if (input.trim().length === 0) {
    return "Fine. Be that way!";
  }

  return "Whatever.";
};

module.exports = Bob;
