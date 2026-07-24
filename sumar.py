<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>Ejercicios</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial; }
        body { padding: 15px; text-align: center; }
        h2 { font-size: 1.3rem; margin-bottom: 15px; }
        #activar { background: #dc2626; color: white; border: none; padding: 12px; border-radius: 8px; width: 100%; font-size: 1.1rem; margin-bottom: 10px; }
        #btnEscuchar { background: #f59e0b; color: white; border: none; padding: 10px; border-radius: 8px; display: none; margin-bottom: 10px; }
        .operacion { font-size: 2.2rem; font-weight: bold; margin: 20px 0; color: #1e40af; }
        .opcion { width: 45%; padding: 12px; margin: 5px 2%; font-size: 1.3rem; border: 2px solid #94a3b8; border-radius: 8px; cursor: pointer; background: white; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #ef4444; background: #fee2e2; color: #b91c1c; }
        #mensaje { margin: 15px 0; font-size: 1.3rem; font-weight: bold; }
        #siguiente { background: #2563eb; color: white; border: none; padding: 12px; border-radius: 8px; width: 100%; font-size: 1.1rem; margin-top: 10px; display: none; }
    </style>
</head>
<body>
    <h2>¿Cuál es el resultado?</h2>
    <button id="activar" onclick="pruebaVoz()">🔊 Toca aquí para activar el sonido</button>
    <button id="btnEscuchar" onclick="leerSuma()">🔊 Escuchar la suma</button>
    <div class="operacion" id="mostrar">7 + 5 = ?</div>

    <button class="opcion" onclick="comprobar(this, 11)">11</button>
    <button class="opcion" onclick="comprobar(this, 12)">12</button>
    <button class="opcion" onclick="comprobar(this, 13)">13</button>
    <button class="opcion" onclick="comprobar(this, 14)">14</button>

    <div id="mensaje"></div>
    <button id="siguiente" onclick="cambiarEjercicio()">➡️ Siguiente ejercicio</button>

    <script>
        const ejercicios = [
            { suma: "7 más 5", texto: "7 + 5 = ?", ok: 12, ops: [11,12,13,14] },
            { suma: "15 más 6", texto: "15 + 6 = ?", ok: 21, ops: [19,20,21,22] },
            { suma: "30 más 10", texto: "30 + 10 = ?", ok: 40, ops: [35,38,40,45] }
        ];
        let indice = 0;
        let vozActiva = false;

        // FUNCIÓN DE VOZ ADAPTADA PARA ANDROID + KODULAR
        function hablar(texto) {
            if(!vozActiva) return;
            window.speechSynthesis.cancel();
            const voz = new SpeechSynthesisUtterance(texto);
            voz.lang = "es-ES";
            voz.rate = 0.9;
            voz.volume = 1;
            // Usar la voz predeterminada del celular
            const voces = window.speechSynthesis.getVoices();
            if(voces.length > 0) voz.voice = voces[0];
            // Ejecutar con retardo para saltar bloqueos
            setTimeout(()=> window.speechSynthesis.speak(voz), 200);
        }

        function pruebaVoz() {
            vozActiva = true;
            document.getElementById('activar').style.display = 'none';
            document.getElementById('btnEscuchar').style.display = 'inline-block';
            hablar("¡Listo! Sonido activado. La suma es " + ejercicios[indice].suma);
        }

        function leerSuma() {
            if(vozActiva) hablar(ejercicios[indice].suma);
        }

        function cargarEjercicio() {
            const e = ejercicios[indice];
            document.getElementById('mostrar').textContent = e.texto;
            document.querySelectorAll('.opcion').forEach((b,i)=>{b.textContent=e.ops[i]; b.className='opcion'; b.disabled=false;});
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
        }

        function comprobar(boton, valor) {
            if(!vozActiva){ alert("Primero activa el sonido"); return; }
            const ok = ejercicios[indice].ok;
            document.querySelectorAll('.opcion').forEach(b=>b.disabled=true);

            if(valor===ok){
                boton.classList.add('correcta');
                const m = "¡Muy bien! Respuesta correcta";
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }else{
                boton.classList.add('incorrecta');
                document.querySelectorAll('.opcion').forEach(b=>{if(parseInt(b.textContent)===ok) b.classList.add('correcta');});
                const m = `No es esa. La correcta es ${ok}`;
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }
            document.getElementById('siguiente').style.display = 'block';
            window.scrollTo(0, document.body.scrollHeight);
        }

        function cambiarEjercicio() {
            indice = (indice+1)%ejercicios.length;
            cargarEjercicio();
            if(vozActiva) hablar("Siguiente ejercicio: " + ejercicios[indice].suma);
        }

        cargarEjercicio();
        // Cargar voces al iniciar
        window.speechSynthesis.onvoiceschanged = () => window.speechSynthesis.getVoices();
    </script>
</body>
</html>
