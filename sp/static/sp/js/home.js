;(function() {
    function ready() {
        var cardImgs = document.querySelectorAll('.card img');
        cardImgs.forEach(function(cardImg){
            if(cardImg.clientWidth >= cardImg.clientHeight){
                cardImg.style.width = 149;
            }
            else{
                cardImg.style.height = 124;
            }
        });

        var descriptions = document.querySelectorAll('.description');
        descriptions.forEach(function(descr){
            if(descr.innerHTML.length > 200){
                descr.innerHTML = descr.innerHTML.slice(0,200) + '...';
            }
        })
    }

    document.addEventListener("DOMContentLoaded", ready);
})();