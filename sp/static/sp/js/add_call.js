;(function () {
    function ready() {
        var element = document.getElementById('id_user_id');
        var temp = document.getElementById('user_id').value;
        for (var i, j = 0; i = element.options[j]; j++) {
            if (i.text == temp) {
                element.selectedIndex = j;
                break;
            }
        }
    }

    document.addEventListener("DOMContentLoaded", ready);
})();
