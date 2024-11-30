alert("sono javascript e sono pronto a servirti ;)")

var nomegiocatore= window.prompt("ciao, inserisci il tuo nome:");
document.getElementById("titolo").innerHTML="benvenuto " + nomegiocatore;

var sceltaUtente;

function presspaper(params) {
    sceltaUtente="carta";
    alert(nomegiocatore+" hai scelto " + sceltaUtente);
}
function pressforbici(params) {
    sceltaUtente="forbici";
    alert(nomegiocatore+" hai scelto " + sceltaUtente);
}
function pressstone(params) {
    sceltaUtente="sasso";
    alert(nomegiocatore+" hai scelto " + sceltaUtente);
}
function verdetto(params) {
    document.getElementById("carta").style.display="none";
    document.getElementById("forbici").style.display="none";
    document.getElementById("sasso").style.display="none";
    document.getElementById("pulsante").style.display="none";
    var sceltacomputer;
    if (sceltaUtente=="carta") {
        sceltacomputer="forbici";
    }
    if (sceltaUtente=="forbici") {
        sceltacomputer="sasso";
    }
    if (sceltaUtente=="sasso") {
        sceltacomputer="carta";
    }
    document.getElementById("titolo").innerHTML=nomegiocatore + " hai Perso!";
    document.getElementById("informazioni").innerHTML=" il computer ha scelto " + sceltacomputer + " tu, hai scelto " + sceltaUtente;
    }