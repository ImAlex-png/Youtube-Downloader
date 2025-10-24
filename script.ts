// Modulo para recoger el valor de lo que venga del input
//Helpers (comunes para todo el boletín)

function $inputValue(id: string) : string{
    const input = document.getElementById(id) as HTMLInputElement; //Lectura
    let result = "";

    if(input){
        result = input.value; //Recojo el valor (aqui es donde leo)
    }

    return result;
}

function $writeNode (id: string, msg: string) : void {
    const nodo = document.getElementById(id) as HTMLElement; //Escritura

    if(nodo){
        nodo.textContent = msg;
    }

}


function downloader() : void {
    const regexp = new RegExp("^https:\/\/"); // Se escapa las barras y no se pone nada mas para que obligaotriamente tenga que poner https:// + lo que sea
    const url = $inputValue("url");

    if(regexp.test(url)){
        window.location.href = url;

    }else{
        $writeNode("error", "URL no valida, introduce otra");
        window.setTimeout(() => $writeNode("error", ""), 5000);
    }

}



