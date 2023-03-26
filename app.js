let input=document.querySelector('.entered-list');
let addBtn=document.querySelector('.add-list');
let tasks=document.querySelector('.tasks');

input.addEventListener('keyup', () => {
    if(input.value.trim() !== 0){
        addBtn.classList.add('active')
    }
    else{
        addBtn.classList.remove('active')
    }
})


addBtn.addEventListener('click',() => {
    if(input.value.trim()!==0){
        let newItem = document.createElement('div');
        newItem.classList.add('item');
        newItem.innerHTML= `
        <p> ${input.value} </p>
        <div class="item-btn">
            <i class="fa-solid fa-pen-to-square"></i>
            <i class="fa-solid fa-xmark"></i>
        </div>
        `
        tasks.appendchild(newItem);
        input.value='';
    }else{
        alert('Please enter a task')
    }
})