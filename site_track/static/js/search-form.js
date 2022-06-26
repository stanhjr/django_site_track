    let CheckModelFilter = document.getElementById('check-model-filter')
    CheckModelFilter.onkeyup = function (){
        let queryString = this.value.toLowerCase()
        let ModelInputs = document.querySelectorAll('[id^="model"]')
        for (let i=0; i < ModelInputs.length; i++){
            let labelText = ModelInputs[i].nextElementSibling.innerHTML
            if(labelText.toLowerCase().startsWith(queryString)){
                ModelInputs[i].closest('li').style.display = 'flex';
            }else {
                ModelInputs[i].closest('li').style.display = 'none';
            }
        }
    }


    let clearModelBtn = document.getElementById("clear-model-filter")
    clearModelBtn.onclick = function () {

        let ModelInputs = document.querySelectorAll('[id^="model"]')
        for (let i=0; i < ModelInputs.length; i++){
            ModelInputs[i].checked = false
        }
    }


    let CheckCategoryFilter = document.getElementById('check-category-filter')
    CheckCategoryFilter.onkeyup = function (){
        let queryString = this.value.toLowerCase()
        let CategoryInputs = document.querySelectorAll('[id^="category"]')

        for (let i=0; i < CategoryInputs.length; i++){
            let labelText = CategoryInputs[i].nextElementSibling.innerHTML

            if(labelText.toLowerCase().startsWith(queryString)){
                CategoryInputs[i].closest('li').style.display = 'flex';
            }else {
                CategoryInputs[i].closest('li').style.display = 'none';
            }
        }
    }

    let clearCategoryBtn = document.getElementById("clear-category-filter")
    clearCategoryBtn.onclick = function () {
        let ModelInputs = document.querySelectorAll('[id^="category"]')
        for (let i=0; i < ModelInputs.length; i++){
            ModelInputs[i].checked = false
        }

    }

    function SetParamForm(key, value){

        if(key.startsWith("model") && document.getElementById("model" + value)){
            document.getElementById("model" + value).checked = true
        }else if(key.startsWith("category") && document.getElementById("category" + value)) {
            document.getElementById("category" + value).checked = true

        }else if(key === "price_max" && document.getElementById("priceMax")) {
            document.getElementById("priceMax").value = value
        }else if (key === "price_min" && document.getElementById("priceMin")){
            document.getElementById("priceMin").value = value
        }
    }

    let CurrentlyUrl = window.location.href
    CurrentlyUrl = CurrentlyUrl.split("?")
    if (CurrentlyUrl.length === 2){
        let QueryParam = CurrentlyUrl[1].split("&")
        for (let i = 0; i < QueryParam.length; i++){
            let Args = QueryParam[i].split("=")
            if (Args.length === 2){
                SetParamForm(Args[0], Args[1])
            }

        }

    }