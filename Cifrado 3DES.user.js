// ==UserScript==
// @name         Encrypt 3DES
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       Millaray Muñoz Penroz
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=instructure.com
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

(function() {
    'use strict';

    const configuracion = {
        mode: CryptoJS.mode.ECB
    }

    // Oración de 9 palabras
    var oracion = "La luz de la luna ilumina la tranqui noche";

    // Llave ENTERO
    var llave = "ENTEROENTEROENTEROENTERO";
    var clave = CryptoJS.enc.Utf8.parse(llave);


    // Función para cifrar una palabra con 3DES
    function cifrarPalabra(palabra, clave) {
        return CryptoJS.TripleDES.encrypt(palabra, CryptoJS.enc.Utf8.parse(clave), configuracion).toString();
    }

    // Dividir la oración en palabras y cifrar cada palabra
    var palabras = oracion.split(" ");
    for (var i = 0; i < palabras.length; i++) {
        var palabraCifrada = cifrarPalabra(palabras[i], llave);
        console.log("Palabra original:", palabras[i]);
        console.log("Palabra cifrada:", palabraCifrada);
    }
})();
