"use strict"

let floatWidget = document.querySelector('.float-widget');
let floatList = document.querySelector('.float-list');
let floatSupElm = floatWidget.lastElementChild;

floatWidget.addEventListener('click', (event)=> {
    let targetClass = event.target.parentElement.children;

    if(targetClass.length == 3) {
        floatSupElm.remove();
        floatWidget.firstElementChild.textContent = 'close';

        const showStyle = {
            opacity: '1',
            bottom: '40px',
            visibility: 'visible',
        }
        Object.assign(floatList.style, showStyle);
    }

    else {
        floatWidget.appendChild(floatSupElm);
        floatWidget.firstElementChild.textContent = 'widgets';
        
        const hideStyle = {
            opacity: '0',
            bottom: '0px',
            visibility: 'hidden',
        }
        Object.assign(floatList.style, hideStyle);
    }
});