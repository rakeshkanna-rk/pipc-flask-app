let count = 0;
const button = document.getElementById('countup');

button.addEventListener('click', () => {
  count++;
  button.textContent = `Count is ${count}`;
});