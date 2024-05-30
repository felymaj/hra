var readlineSync = require("readline-sync") 
var jmeno = readlineSync.question("Jak se jmenuješ? ");

function Hello(){
    return "Hello " + jmeno       
}

console.log(Hello())

var readlineSync = require("readline-sync") 
var Kostka = readlineSync.question("KOstká má čísel? ");
Kostka = parseInt(Kostka)

function random(strany){
    let para = Math.random()*strany
    

    return Math.ceil(para)
}

while(poradi<100){
    poradi=poradi + 1


console.log (`Kostce #${poradi} spadlo ${random(poradi)}`)
}

