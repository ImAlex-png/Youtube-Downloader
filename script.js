// Modulo para recoger el valor de lo que venga del input
//Helpers (comunes para todo el boletín)
function $inputValue(id) {
    var input = document.getElementById(id); //Lectura
    var result = "";
    if (input) {
        result = input.value; //Recojo el valor (aqui es donde leo)
    }
    return result;
}
function $writeNode(id, msg) {
    var nodo = document.getElementById(id); //Escritura
    if (nodo) {
        nodo.textContent = msg;
    }
}
function downloader() {
    var regexp = new RegExp("^https:\/\/"); // Se escapa las barras y no se pone nada mas para que obligaotriamente tenga que poner https:// + lo que sea
    var url = $inputValue("url");
    if (regexp.test(url)) {
        window.location.href = url;
    }
    else {
        $writeNode("error", "URL no valida, introduce otra");
        window.setTimeout(function () { return $writeNode("error", ""); }, 5000);
    }
}
