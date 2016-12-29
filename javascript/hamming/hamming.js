function Hamming() {

  this.compute = function(strandA, strandB){
    if (strandA.length !== strandB.length) {
      throw new Error("DNA strands must be of equal length.");
    }

    distance = 0;
    for (var i = 0; i < strandA.length; i++) {
      if (strandA.charAt(i) !== strandB.charAt(i)) {
        distance++;
      }
    }
    return distance;
  };
}

module.exports = Hamming;
