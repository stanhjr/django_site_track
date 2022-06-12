"use strict"

document.querySelectorAll('.select-data').forEach((item)=> {
    item.addEventListener('click', function() {

        let optionList = document.querySelector('.option-list');
        let selectHeight = parseInt(optionList.style.height);
        let scrollHeight = optionList.scrollHeight;

        if(selectHeight != scrollHeight) {
            this.nextElementSibling.style.height = scrollHeight + 'px';
            item.parentElement.classList.add('selected');
        }
        else { 
            this.nextElementSibling.style.height = '0px'; 
            item.parentElement.classList.remove('selected');
        }
    })
})

document.querySelectorAll('.option-item').forEach((item)=> {
    item.addEventListener('click', function() {

        let selectImage = document.querySelector('.select-image');
        let selectText = document.querySelector('.select-text');

        let optionImage = item.firstElementChild.children[0].getAttribute('src');
        let optionText = item.firstElementChild.children[1].textContent;

        let imgSource = (selectImage.getAttribute('src') !== optionImage);
        let txtSource = (selectText.textContent !== optionText);

        if(imgSource && txtSource) {
            selectImage.setAttribute('src', optionImage);
            selectText.textContent = optionText;
        }
    })
})

