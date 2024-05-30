
var request = require('sync-request');
var res = request('GET', 'https://jsonplaceholder.typicode.com/posts', {
});

var users =  JSON.parse((res.getBody("utf-8")));

const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('Zadejte ID uživatele: ', (inputId) => {
  var userId = parseInt(inputId);
  var user = users.find(u => u.userId === userId);
  var userData = {};
  if (user) {
    userData.id = user.id;
    userData.title = user.title;
    userData.body = user.body;

    console.log('ID: ' + userData.id);
    console.log('Title: ' + userData.title);
    console.log('Body: ' + userData.body);
  } else {
    console.log('Uživatel s ID ' + userId + ' nebyl nalezen.');
  }
  readline.close();
});
