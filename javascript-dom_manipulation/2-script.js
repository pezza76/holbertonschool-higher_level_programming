const red_header = document.querySelector('#red_header')

red_header.addEventListener('click', function() {
    const header = document.querySelector('header');
    header.classList.add('red')
})
