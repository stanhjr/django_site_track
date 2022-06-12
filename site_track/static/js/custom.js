"use strict"

function scrollToggle(dataObject) {
    const { selectData, toggleData, scrollDigit } = dataObject;

    window.addEventListener('scroll', function() {
        const selectElement = document.querySelector(selectData);
        if(window.pageYOffset > scrollDigit) selectElement?.classList.add(toggleData);
        else selectElement?.classList.remove(toggleData);
    })
}

// for header bar fixed
scrollToggle({
    selectData: '.header-part',  // selectable class or id name with .(dots) or #(hash)
    toggleData: 'sticky',  // toggle class or id name without .(dots) or #(hash)
    scrollDigit: '0',  // Scroll position number from above
});


// for product single page btns fixed
scrollToggle({
    selectData: '.product-single-scrollspy-btns',  // selectable class or id name with .(dots) or #(hash)
    toggleData: 'fixed',  // toggle class or id name without .(dots) or #(hash)
    scrollDigit: '1150',  // Scroll position number from above
});



function clickToggle(dataObject) {
    const { selectData, toggleData } = dataObject;
    const selectElement = document.querySelectorAll(selectData);

    for(let i = 0; i < selectElement.length; i++) {
        selectElement[i].addEventListener('click', function() {
            if(selectElement[i].className.includes(toggleData)) {
                selectElement[i].classList.remove(toggleData);
            }
            else selectElement[i].classList.add(toggleData);
        })
    }
}

// for favorite button active 
clickToggle({
    selectData: '.favorite',  // selectable class or id name with .(dots) or #(hash)
    toggleData: 'active',  // toggle class or id name without .(dots) or #(hash)
});

// for compare button active 
clickToggle({
    selectData: '.compare',  // selectable class or id name with .(dots) or #(hash)
    toggleData: 'active',  // toggle class or id name without .(dots) or #(hash)
});


// for sidebar layout open & closing
function sidebarLayout() {
    const sidebarPart = document.querySelector('.sidebar-part');
    const sidebarOpen = document.querySelector('.sidebar-open');
    const sidebarClose = document.querySelector('.sidebar-close');
    const backdrop = document.querySelector('.backdrop');
    const body = document.querySelector('body');

    // sidebar opening
    sidebarOpen.addEventListener('click', function () {
        sidebarPart.classList.add('open');
        backdrop.classList.add('active');
        body.style.overflowY = 'hidden';
    })

    // sidebar closing
    sidebarClose.addEventListener('click', function () {
        sidebarPart.classList.remove('open');
        backdrop.classList.remove('active');
        body.style.overflowY = 'scroll';
    })

    // backdrop closing
    backdrop.addEventListener('click', function () {
        sidebarPart.classList.remove('open');
        backdrop.classList.remove('active');
        body.style.overflowY = 'scroll';
    })
}
sidebarLayout();


// for comment action hide & show
function dotsAction(dotsBtn) {
    const actionBtn = document.querySelectorAll(dotsBtn);

    for (let i = 0; i < actionBtn.length; i++) {
        actionBtn[i].addEventListener('click', function () {
            const actionIcon = actionBtn[i].firstElementChild;
            const actionList = actionBtn[i].nextElementSibling;

            if (actionIcon.textContent == 'close') {
                actionBtn[i].classList.remove('active');
                actionList.classList.remove('show');
                actionIcon.innerText = 'more_vert';
            }
            else {
                actionBtn[i].classList.add('active');
                actionList.classList.add('show');
                actionIcon.innerText = 'close';
            }
        })
    }
}
dotsAction('.comment-action-btn');
dotsAction('.review-action-btn');


// For advance search option
document.querySelector('.header-search').lastElementChild.addEventListener('click', (event) => {
    if (event.target.textContent !== 'tune') {
        event.target.offsetParent.classList.remove('active')
        event.target.textContent = 'tune'
    }
    else {
        event.target.offsetParent.classList.add('active')
        event.target.textContent = 'close'
    }
})


// For responsive search bar
document.querySelector('.responsive-srch').addEventListener('click', (event) => {
    const headerForm = document.querySelector('.header-form');

    if (event.target.textContent !== 'search') {
        headerForm.style.display = 'none';
        event.target.textContent = 'search';
    }
    else {
        headerForm.style.display = 'block';
        event.target.textContent = 'close';
    }
})

// For clickable active content
function selection(selective) {
    let selectActive = document.querySelectorAll(selective);

    for (let i = 0; i < selectActive.length; i++) {
        selectActive[i].addEventListener('click', () => {
            selectActive.forEach((event) => event.classList.remove('active'))
            selectActive[i].classList.add('active');
        })
    }
}
selection('.create-price-card')
selection('.create-pay-card')



function cancelValue() {
    const fileCancel = document.querySelectorAll('.file-cancel');

    fileCancel.forEach((ele)=>{
        ele.parentElement.querySelector('.file-input').addEventListener('change', function(event) {
            ele.parentElement.querySelector('.file-cancel').style.display = 'block'
            console.log(ele.parentElement.querySelector('.file-cancel'))
        })

        ele.addEventListener('click', function(event) {
            event.target.parentElement.querySelector('.file-input').value = ''
            event.target.parentElement.querySelector('.file-cancel').style.display = 'none'
        })
    })
}
cancelValue()


function slickSliderDotsString() {
    const owlDot = document.querySelectorAll('.slick-dots li');

    Array.from(owlDot).map((item, index)=> {
        const owlDotIndex = index + 1;
        item.children[0].textContent = '0' + owlDotIndex;
    })
}
slickSliderDotsString();