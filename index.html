<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Ejercicios de Sumas</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: Arial; padding: 1rem; background: #fff; text-align: center; }
        h2 { font-size: 1.3rem; margin-bottom: 1rem; color: #222; }
        #activarVoz { background: #ef4444; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 8px; font-size: 1.1rem; margin-bottom: 1rem; cursor: pointer; width: 100%; }
        #btnVoz { background: #f59e0b; color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 8px; font-size: 1rem; margin-bottom: 1rem; cursor: pointer; display: none; }
        .operacion { font-size: 2.2rem; font-weight: bold; margin: 1.5rem 0; color: #1e40af; }
        .opcion { display: inline-block; width: 45%; padding: 1rem; margin: 0.5rem 2%; font-size: 1.3rem; border: 2px solid #94a3b8; border-radius: 8px; cursor: pointer; background: white; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #ef4444; background: #fee2e2; color: #b91c1c; }
        #mensaje { margin-top: 1.5rem; font-size: 1.4rem; font-weight: bold; color: #166534; }
        #siguiente { margin-top: 1rem; background: #2563eb; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 8px; cursor: pointer; font-size: 1.1rem; width: 100%; display: none; }
    </style>
</head>
<body>
    <h2>¿Cuál es el resultado?</h2>
    <!-- BOTÓN OBLIGATORIO PARA ACTIVAR EL SONIDO -->
    <button id="activarVoz" onclick="activarSonido()">🔊 Toca aquí para activar el sonido</button>
    <button id="btnVoz" onclick="leerSuma()">🔊 Escuchar la suma</button>
    <div class="operacion" id="mostrarSuma">7 + 5 = ?</div>

    <button class="opcion" onclick="comprobar(this, 11)">11</button>
    <button class="opcion" onclick="comprobar(this, 12)">12</button>
    <button class="opcion" onclick="comprobar(this, 13)">13</button>
    <button class="opcion" onclick="comprobar(this, 14)">14</button>

    <div id="mensaje"></div>
    <button id="siguiente" onclick="cambiarEjercicio()">Siguiente ejercicio</button>

    <script>
        const ejercicios = [
            { suma: "7 más 5", texto: "7 + 5 = ?", respuestaBuena: 12, opciones: [11,12,13,14] },
            { suma: "15 más 6", texto: "15 + 6 = ?", respuestaBuena: 21, opciones: [19,20,21,22] },
            { suma: "30 más 10", texto: "30 + 10 = ?", respuestaBuena: 40, opciones: [35,38,40,45] }
        ];
        let indice = 0;
        let vozActiva = false;

        function hablar(texto) {
            if(!vozActiva) return;
            window.speechSynthesis.cancel();
            const voz = new SpeechSynthesisUtterance(texto);
            voz.lang = "es-ES";
            voz.rate = 0.9;
            // Forzar reproducción
            voz.volume = 1;
            window.speechSynthesis.speak(voz);
        }

        function activarSonido() {
            vozActiva = true;
            document.getElementById('activarVoz').style.display = 'none';
            document.getElementById('btnVoz').style.display = 'inline-block';
            // Prueba de voz al activar
            hablar("Sonido activado. Escucha la suma");
            setTimeout(()=> hablar(ejercicios[indice].suma), 1500);
        }

        function leerSuma() {
            if(vozActiva) hablar(ejercicios[indice].suma);
        }

        function cargarSuma() {
            const e = ejercicios[indice];
            document.getElementById('mostrarSuma').textContent = e.texto;
            document.querySelectorAll('.opcion').forEach((b,i)=>{
                b.textContent = e.opciones[i];
                b.className = 'opcion';
                b.disabled = false;
            });
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
        }

        function comprobar(boton, valor) {
            if(!vozActiva) {
                alert("Primero activa el sonido con el botón rojo");
                return;
            }
            const ok = ejercicios[indice].respuestaBuena;
            document.querySelectorAll('.opcion').forEach(b=>b.disabled=true);

            if(valor === ok){
                boton.classList.add('correcta');
                const m = "¡Muy bien! Respuesta correcta";
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }else{
                boton.classList.add('incorrecta');
                document.querySelectorAll('.opcion').forEach(b=>{
                    if(parseInt(b.textContent) === ok) b.classList.add('correcta');
                });
                const m = `No es esa. La respuesta correcta es ${ok}`;
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }

            document.getElementById('siguiente').style.display = 'block';
        }

        function cambiarEjercicio() {
            indice = (indice + 1) % ejercicios.length;
            cargarSuma();
            if(vozActiva) hablar(ejercicios[indice].suma);
        }

        cargarSuma();
    </script>
</body>
</html>
