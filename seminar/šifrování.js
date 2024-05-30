let input = "heslo";
let skok = 3;
let input2 = 0;

function sifra(Slovo, skok2){
    let text = Slovo;
    let novyText = "";
    for (let i = 0; i < text.length; i++){ 
        let Znak = text[i];
        let kodASCII = Znak.charCodeAt(0);
        let znakZKodu = String.fromCharCode((kodASCII + skok2) % 256); 
        novyText += znakZKodu;
    }
    return novyText;
}

function desifra(Slovo, skok2){
    let text = Slovo;
    let novyText = "";
    for (let i = 0; i < text.length; i++){ 
        let Znak = text[i];
        let kodASCII = Znak.charCodeAt(0);
        let znakZKodu = String.fromCharCode((kodASCII - skok2 + 256) % 256); 
        novyText += znakZKodu;
    }
    return novyText;
}

if (input2 === 0) {
    let vysledek = sifra(input, skok);
    console.log("Zakódovaný text: " + vysledek);
} 
else if (input2 === 1){
    let vysledek = desifra(input, skok);
    console.log("Dešifrovaný text: " + vysledek);
}