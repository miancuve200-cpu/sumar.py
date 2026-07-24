<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="mobile-web-app-capable" content="yes">
    <title>Ejercicios</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial, sans-serif; }
        html, body { height: 100%; overflow-x: hidden; padding: 10px; background: #fff; text-align: center; }

        h2 { font-size: 1.2rem; margin: 10px 0; color: #222; }
        #activarSonido { background: #dc2626; color: white; border: none; padding: 12px; border-radius: 8px; font-size: 1rem; width: 100%; margin-bottom: 10px; cursor: pointer; }
        #btnLeer { background: #f59e0b; color: white; border: none; padding: 10px; border-radius: 8px; font-size: 0.95rem; margin-bottom: 10px; cursor: pointer; display: none; }
        .operacion { font-size: 2rem; font-weight: bold; margin: 15px 0; color: #1e40af; }
        .opcion { display: inline-block; width: 46%; padding: 12px; margin: 4px 1%; font-size: 1.2rem; border: 2px solid #94a3b8; border-radius: 8px; cursor: pointer; background: white; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #ef4444; background: #fee2e2; color: #b91c1c; }
        #mensaje { margin: 12px 0; font-size: 1.2rem; font-weight: bold; color: #166534; min-height: 30px; }
        #siguiente { background: #2563eb; color: white; border: none; padding: 12px; border-radius: 8px; font-size: 1.1rem; width: 100%; margin-top: 8px; cursor: pointer; display: none; }
    </style>
</head>
<body>
    <h2>¿Cuál es el resultado?</h2>

    <!-- BOTÓN OBLIGATORIO PARA ACTIVAR SONIDO EN ANDROID -->
    <button id="activarSonido" onclick="activarVoz()">🔊 Toca aquí para activar el sonido</button>
    <button id="btnLeer" onclick="leer()">🔊 Escuchar la suma</button>

    <div class="operacion" id="sumaTexto">7 + 5 = ?</div>

    <button class="opcion" onclick="verificar(this, 11)">11</button>
    <button class="opcion" onclick="verificar(this, 12)">12</button>
    <button class="opcion" onclick="verificar(this, 13)">13</button>
    <button class="opcion" onclick="verificar(this, 14)">14</button>

    <div id="mensaje"></div>
    <!-- BOTÓN SIEMPRE VISIBLE Y ANCHO -->
    <button id="siguiente" onclick="siguienteEjercicio()">➡️ Siguiente ejercicio</button>

    <script>
        const lista = [
            { suma: "7 más 5", ver: "7 + 5 = ?", ok: 12, ops: [11,12,13,14] },
            { suma: "15 más 6", ver: "15 + 6 = ?", ok: 21, ops: [19,20,21,22] },
            { suma: "30 más 10", ver: "30 + 10 = ?", ok: 40, ops: [35,38,40,45] }
        ];
        let actual = 0;
        let vozLista = false;

        // FUNCIÓN DE VOZ SEGURA PARA ANDROID
        function hablar(texto) {
            if(!vozLista) return;
            window.speechSynthesis.cancel();
            const voz = new SpeechSynthesisUtterance(texto);
            voz.lang = "es-ES";
            voz.rate = 0.9;
            voz.volume = 1;
            // Forzar ejecución
            setTimeout(()=> window.speechSynthesis.speak(voz), 100);
        }

        function activarVoz() {
            vozLista = true;
            document.getElementById('activarSonido').style.display = 'none';
            document.getElementById('btnLeer').style.display = 'inline-block';
            hablar("Sonido activado. La suma es: " + lista[actual].suma);
        }

        function leer() {
            if(vozLista) hablar(lista[actual].suma);
        }

        function cargar() {
            const e = lista[actual];
            document.getElementById('sumaTexto').textContent = e.ver;
            const botones = document.querySelectorAll('.opcion');
            botones.forEach((b,i)=>{
                b.textContent = e.ops[i];
                b.className = 'opcion';
                b.disabled = false;
            });
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
        }

        function verificar(boton, valor) {
            if(!vozLista){
                alert("Primero activa el sonido con el botón rojo");
                return;
            }
            const correcta = lista[actual].ok;
            document.querySelectorAll('.opcion').forEach(b=>b.disabled=true);

            if(valor === correcta){
                boton.classList.add('correcta');
                const m = "¡Muy bien! Respuesta correcta";
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }else{
                boton.classList.add('incorrecta');
                document.querySelectorAll('.opcion').forEach(b=>{
                    if(parseInt(b.textContent) === correcta) b.classList.add('correcta');
                });
                const m = `No es esa. La correcta es ${correcta}`;
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }

            // FORZAR QUE APAREZCA EL BOTÓN
            document.getElementById('siguiente').style.display = 'block';
            window.scrollTo(0, document.body.scrollHeight);
        }

        function siguienteEjercicio() {
            actual = (actual + 1) % lista.length;
            cargar();
            if(vozLista) hablar("Siguiente ejercicio: " + lista[actual].suma);
        }

        cargar();
    </script>
</body>
</html>
