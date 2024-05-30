print

const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.question("Kolik ti je: ", (age) => {
  if (age >= 18) {
    console.log("můžeš jit in");
  } else {
    console.log("nemužeš nevadi");
  }
  readline.close();
});
ques