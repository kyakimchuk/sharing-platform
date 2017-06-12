;(function() {
    function ready() {
        var cardImg = document.querySelector('.card img');
        if(cardImg.clientWidth >= cardImg.clientHeight){
                cardImg.style.minWidth = 397;
                cardImg.style.maxWidth = 800;
        }
        else{
            cardImg.style.height = 331;
        }
    }

    document.addEventListener("DOMContentLoaded", ready);
})();