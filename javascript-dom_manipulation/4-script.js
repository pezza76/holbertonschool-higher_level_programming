const add_list = document.querySelector('#add_item');
const my_list = document.querySelector('.my_list')

add_list.addEventListener('click', function() {
    const new_item = document.createElement('li');
    new_item.textContent = 'Item';
    my_list.appendChild(new_item);
})