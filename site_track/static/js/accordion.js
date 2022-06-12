"use strict"

function accordion(selectClass, firstElement) {
    const selectElement = document.querySelectorAll(selectClass);

    if(firstElement) {
        const activeElement = selectElement[0].lastElementChild;
        activeElement.style.height = activeElement.scrollHeight + 'px';
    }

    for(let i = 0; i < selectElement.length; i++) {
        selectElement[i].firstElementChild.addEventListener('click', ()=> {
            
            const expandElement = selectElement[i].lastElementChild;
            const elementList = selectElement[i].parentElement.children;
            const clickIndex = Array.from(elementList).indexOf(selectElement[i])

            if(parseInt(expandElement.style.height) !== expandElement.scrollHeight) {
                for(let j = 0; j < elementList.length; j++) {
                    if(j !== clickIndex) {
                        selectElement[j].classList.remove('active'); 
                        selectElement[j].lastElementChild.style.height = '0px';
                    }
                }
                selectElement[i].classList.add('active');
                expandElement.style.height = expandElement.scrollHeight + 'px'
            }
            else {
                selectElement[i].classList.remove('active');
                expandElement.style.height = '0px'
            }
        })
    }
}
accordion('.accordion-item', false);
