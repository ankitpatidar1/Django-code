
function UserAction() {
    // var xhttp = new XMLHttpRequest();
    debugger
    var arr = []
    var x = document.forms[0];
    var x_len = x.elements.length;
    for(i=1; i < x_len; i++){
        arr.push(x.elements[i].value)
    } 
    console.log(arr)
}