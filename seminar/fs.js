function Sifra(vgjzct) {
    let sifra = ""
     for (i = 0; i < heslo.length; i++) {
         //Každej symbol po symbolu
         let znak = heslo[i]
         //let kodAbededy = text.charCodeAt
         let kodAbecedy = znak.charCodeAt(0);
         console.log(`Znak ${znak} je na pozici ${i} : ${kodAbecedy}`)
         kodAbecedy = kodAbecedy + parseInt(skok)
         let znakZKodu = String.fromCharCode(kodAbecedy)
         sifra += znakZKodu
         console.log(`Kód ${kodAbecedy} je ${znakZKodu}`)
     }
     console.log(`Sifra je ${sifra}`)
 }
 
 let heslo = prompt("Zvol text")
 let okolikskocit = prompt("O kolik chceš skočit na šifře?")
 Sifra(heslo, okolikskocit)