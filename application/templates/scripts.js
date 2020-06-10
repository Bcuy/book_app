document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#submit').disabled = true;

  document.querySelector('#task').onkeyup = function () {
    document.querySelector('#submit').disabled = false;

  }

  document.querySelector('#new-task').onsubmit = function () {

    const li = document.createElement('li');
    li.innerHTML = document.querySelector('#task').value;

    document.querySelector('#tasks').append(li);

    document.querySelector('#task').value = ''

    document.querySelector('#submit').disabled = true

    return false

    }

});

let x = prompt('What is your age?')

if ((x >= 18) && (x <= 35)) {
  status = 'Target demo'
  console.log(status);
} else {
  status = 'Not target demo'
  console.log(status);
}
