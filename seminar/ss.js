function random(Strana){ 
    let cislo = Math.random()*Strana

    return Math.ceil(cislo)
}


for(let poradi = 1; poradi<100; poradi+=1){
    console.log (`Kostce #${poradi} spadlo  ${random(poradi)}`)
}