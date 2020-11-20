document.getElementById('story-form').onsubmit = function () {
    let madLib = document.getElementById("madLib");
        madLib.innerHTML = "fuck";
    let genre = document.getElementById("genre").value;
    let conflict = document.getElementById("conflict").value;
    let resolution = document.getElementById("resolution").value;
    let protagonist = document.getElementById("protagonist").value;
    let adjective = document.getElementById("adjective").value;
    let verb = document.getElementById("verb").value;
    let propernoun = document.getElementById("propernoun").value;
    let adverb = document.getElementById("adverb").value;
    let noun = document.getElementById("noun").value;


    if (genre === "horror") {
        madLib.innerHTML = "If zombies attacked a picnic, what would they " + verb + " eat? Everybody knows zombies love to "
            + verb + " " + noun + ", but did you know they also enjoy " + propernoun + " and even frogs? The best "
            + noun + " for a zombie picnic is when the moon is " + adjective + ". At least one zombie will bring blood "
            + " to drink, and it's not a picnic without " + protagonist + " with extra blood on top. After eating zombies will "
            + verb + " " + adjective + " games like kick the body part.";
    } else if (genre === "action") {
        madLib.innerText = "A vacation is when you take a trip to some " + adjective + " place with your "
            + adjective + " family. Usually you go to some place that is near a/an " + noun + " or up a/an "
            + noun + ". A good vacation place is one where you can ride " + propernoun + " or play " + noun +
            " or go hunting for deer. I like to spend my time climbing " + adverb + ".";
    } else if (genre === "comedy") {
        madLib.innerText = "Unicorns aren't like other " + propernoun + " they're " + adjective + ". They look like "
            + protagonist + ", with " + noun + " for feet and a huge mane of hair. But unicorns are rainbow and have a "
            + adjective + " " + noun + " on their heads. Some " + propernoun + " don't believe in them. I would love to "
            + verb + " a unicorn to faraway lands.";
    } else if (genre === "scifi") {
        madLib.innerText = "On a starship traveling across the galaxy, " + protagonist + "  is attempting to find a new "
            + noun + ". Navigating while " + verb + " will be difficult, but with the help of "
            + propernoun + ", this " + adjective + " adventure will be like nothing ever seen before.";
    } else if (genre === "fantasy") {
        madLib.innerText = "After growing up as a dairy farmer, " + protagonist + " finds themselves being attacked by a "
            + noun + ". This attack causes the " + adjective + " farmer to " + verb + " a nearby town called "
            + propernoun + ". This is where" + protagonist + "'s story begins...";
    }else {
        console.log(onerror);
    }
    return false
}