function generateMadLib() {
    var madLib = document.getElementById("madLib");
    var genre = document.getElementById("genre").value;
    var conflict = document.getElementById("conflict").value;
    var resolution = document.getElementById("resolution").value;
    var protagonist = document.getElementById("protagonist").value;
    var adjective = document.getElementById("adjective").value;
    var propernoun = document.getElementById("propernoun").value;
    var adverb = document.getElementById("adverb").value;
    var noun = document.getElementById("noun").value;
    



    madLib.innerHTML = "A vacation is when you take a trip to some " + adjective + " place with your " + adjective + " family. Usually you go to some place that is near a/an " + noun + " or up/an " + noun + ". A good vacation place is one where you can ride " + propernoun + " or play " + noun + " or go hunting for deer. I like to spend my time climbing " + adverb;
}
