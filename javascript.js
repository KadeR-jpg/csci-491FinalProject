function generateMadLib() {
    let madLib = document.getElementById("madLib");
    let genre = document.getElementById("genre").value;
    let conflict = document.getElementById("conflict").value;
    let resolution = document.getElementById("resolution").value;
    let protagonist = document.getElementById("protagonist").value;
    let adjective = document.getElementById("adjective").value;
    let propernoun = document.getElementById("propernoun").value;
    let adverb = document.getElementById("adverb").value;
    let noun = document.getElementById("noun").value;
    madLib.innerHTML = "A vacation is when you take a trip to some " + adjective + " place with your " + adjective +
        " family. Usually you go to some place that is near a/an " + noun + " or up/an " + noun + ". A good vacation " +
        "place is one where you can ride " + propernoun + " or play " + noun + " or go hunting for deer. I like to " +
        "spend my time climbing " + adverb;
}
