// ==UserScript==
// @name         Decrypt2 3DES
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Millaray Muñoz Penroz
// @match        https://texto-nuevo.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=instructure.com
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

(function() {
    'use strict';

    // Obtén el texto de la página
    var textoOriginal = document.body.textContent || document.body.innerText;

    // Función para extraer las mayúsculas y concatenarlas
    function extraerMayusculas(texto) {
        var mayusculas = texto.replace(/[^A-Z]/g, ''); // Expresión regular para obtener solo las mayúsculas
        return mayusculas;
    }

    // Llama a la función con el texto de la página
    var llaveGenerada = extraerMayusculas(textoOriginal);


    //Filtra solo los divs que tienen un atributo de ID
    var divsConId = Array.from(document.getElementsByTagName('div')).filter(function(div) {
        return div.id !== '';
    });

    // Cuenta la cantidad de elementos div en la página
    var cantidadDeDivs = divsConId.length;

    // Muestra la información en la consola
    console.log("La llave es:", llaveGenerada);
    console.log("Los mensajes cifrados son:", cantidadDeDivs);

    const configuracion = {
       mode: CryptoJS.mode.ECB
   };

     // Itera sobre los elementos div con ID y descifra el valor del ID
    divsConId.forEach(function(div) {
        var idValue = div.id;
        const decryptedValue = CryptoJS.TripleDES.decrypt(idValue, CryptoJS.enc.Utf8.parse(llaveGenerada), configuracion).toString(CryptoJS.enc.Utf8);

        // Muestra la información en la consola
        console.log(idValue, decryptedValue);

        // Muestra las palabras descifradas en la página
        div.innerText = decryptedValue;
    });

})();
