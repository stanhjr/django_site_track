"use strict"

function navTabs() {
    const navList = document.querySelector('.create-nav-list');
    const tabList = document.querySelector('.create-ads-form');

    for(let i = 0; i < navList.childElementCount; i++) {
        const navChild = navList.children[i];
        const tabChild = tabList.children[i];

        navChild.addEventListener('click', function() {

            Array.from(navList.children).map((elem)=> elem.classList.remove('active'));
            Array.from(tabList.children).map((elem)=> elem.classList.remove('active'));

            navChild.classList.add('active');
            tabChild.classList.add('active');

            for(let pos = 0; pos < navList.childElementCount; pos++) {
                
                if(pos < i) navList.children[pos].classList.add('complete');
                else navList.children[pos].classList.remove('complete');
            }
        })
    }
}
navTabs()