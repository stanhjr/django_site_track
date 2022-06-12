"use strict"

let navItem = document.getElementsByClassName('nav-item');
let navLink = document.getElementsByClassName('nav-link');
let dropList = document.getElementsByClassName('drop-list');

const openDwopDown = () => {
    for (let i = 0; i < navItem.length; i++) {
        if (navItem[i].querySelector('ul') != null) {
            let selectChildDropDown = navItem[i].querySelector('ul')
            navItem[i].addEventListener('click', () => {
                let selectHeight = parseInt(selectChildDropDown.style.height);
                let scrollHeight = selectChildDropDown.scrollHeight;
                closeAllDropDown();
                removeAllActiveClass();
                if (selectHeight != scrollHeight) {
                    selectChildDropDown.style.height = selectChildDropDown.scrollHeight + 'px';
                    navItem[i].classList.add('dropdown');
                    
                }
                else {
                    console.log(selectHeight, scrollHeight)

                    selectChildDropDown.style.height = '0px';
                    navItem[i].classList.remove('dropdown');
                }
            })
        }
    }
}

const removeAllActiveClass = () => {
    for (let i = 0; i < navItem.length; i++) {
        navItem[i].classList.remove('dropdown');
    }
}
const closeAllDropDown = () => {
    for (let q = 0; q < dropList.length; q++) {
        dropList[q].style.height = '0px';
    }
}

// Main Call
openDwopDown();