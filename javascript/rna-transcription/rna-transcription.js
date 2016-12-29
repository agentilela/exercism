var DnaTranscriber = function() {

  strandData = {
    "C": "G",
    "G": "C",
    "A": "U",
    "T": "A"
  };

  this.toRna = function(strand) {
    rnaStrand = "";
    for (var i = 0; i < strand.length; i++) {
      rnaStrand += strandData[strand.charAt(i)];
    }
    return rnaStrand;
  };

};

module.exports = DnaTranscriber;
