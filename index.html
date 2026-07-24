<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0">
    <title>Ejercicios de Matemáticas</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; font-family: Arial; }
        body { padding: 15px; text-align: center; background: #fff; }
        h1 { font-size: 1.5rem; margin-bottom: 20px; color: #222; }
        h2 { font-size: 1.3rem; margin-bottom: 15px; }

        /* MENÚ PRINCIPAL */
        #menu { display: block; }
        .btnOperacion { display: block; width: 90%; max-width: 400px; margin: 10px auto; padding: 15px; font-size: 1.3rem; border: none; border-radius: 10px; cursor: pointer; color: white; font-weight: bold; }
        #btnSuma { background: #16a34a; }
        #btnResta { background: #2563eb; }
        #btnMulti { background: #f59e0b; }
        #btnDivi { background: #ef4444; }

        /* EJERCICIOS */
        #ejercicios { display: none; }
        #volver { background: #6b7280; color: white; border: none; padding: 10px 20px; border-radius: 8px; margin-bottom: 15px; cursor: pointer; font-size: 1rem; }
        #activarSonido { background: #dc2626; color: white; border: none; padding: 12px; border-radius: 8px; width: 100%; font-size: 1.1rem; margin-bottom: 10px; }
        #btnLeer { background: #f59e0b; color: white; border: none; padding: 10px; border-radius: 8px; display: none; margin-bottom: 10px; }
        .operacion { font-size: 2rem; font-weight: bold; margin: 15px 0; color: #1e40af; }
        .opcion { display: inline-block; width: 45%; padding: 12px; margin: 5px 2%; font-size: 1.2rem; border: 2px solid #94a3b8; border-radius: 8px; cursor: pointer; background: white; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #ef4444; background: #fee2e2; color: #b91c1c; }
        #mensaje { margin: 12px 0; font-size: 1.2rem; font-weight: bold; color: #166534; min-height: 30px; }
        #siguiente { background: #2563eb; color: white; border: none; padding: 12px; border-radius: 8px; font-size: 1.1rem; width: 100%; margin-top: 8px; cursor: pointer; display: none; }
    </style>
</head>
<body>

    <!-- MENÚ PRINCIPAL -->
    <div id="menu">
        <h1>Elige la operación</h1>
        <button class="btnOperacion" id="btnSuma" onclick="cargarOperacion('suma')">➕ SUMAS</button>
        <button class="btnOperacion" id="btnResta" onclick="cargarOperacion('resta')">➖ RESTAS</button>
        <button class="btnOperacion" id="btnMulti" onclick="cargarOperacion('multiplicacion')">✖️ MULTIPLICACIONES</button>
        <button class="btnOperacion" id="btnDivi" onclick="cargarOperacion('division')">➗ DIVISIONES</button>
    </div>

    <!-- ZONA DE EJERCICIOS -->
    <div id="ejercicios">
        <button id="volver" onclick="volverMenu()">⬅️ Volver al menú</button>
        <h2 id="tituloOperacion"></h2>
        <button id="activarSonido" onclick="activarVoz()">🔊 Toca aquí para activar el sonido</button>
        <button id="btnLeer" onclick="leer()">🔊 Escuchar el ejercicio</button>
        <div class="operacion" id="textoEjercicio"></div>

        <button class="opcion" onclick="verificar(this, 0)"></button>
        <button class="opcion" onclick="verificar(this, 0)"></button>
        <button class="opcion" onclick="verificar(this, 0)"></button>
        <button class="opcion" onclick="verificar(this, 0)"></button>

        <div id="mensaje"></div>
        <button id="siguiente" onclick="siguienteEjercicio()">➡️ Siguiente ejercicio</button>
    </div>

    <script>
        // 10 EJERCICIOS PARA CADA OPERACIÓN
        const bancos = {
            suma: [
                { voz: "dos más tres", ver: "2 + 3 = ?", ok: 5, ops: [4,5,6,7] },
                { voz: "siete más cinco", ver: "7 + 5 = ?", ok: 12, ops: [10,11,12,13] },
                { voz: "diez más ocho", ver: "10 + 8 = ?", ok: 18, ops: [16,17,18,19] },
                { voz: "quince más seis", ver: "15 + 6 = ?", ok: 21, ops: [19,20,21,22] },
                { voz: "veinte más diez", ver: "20 + 10 = ?", ok: 30, ops: [25,28,30,35] },
                { voz: "nueve más nueve", ver: "9 + 9 = ?", ok: 18, ops: [16,17,18,19] },
                { voz: "veinticinco más cinco", ver: "25 + 5 = ?", ok: 30, ops: [28,29,30,31] },
                { voz: "treinta más veinte", ver: "30 + 20 = ?", ok: 50, ops: [45,48,50,55] },
                { voz: "cuarenta más doce", ver: "40 + 12 = ?", ok: 52, ops: [50,51,52,53] },
                { voz: "cincuenta más veinticinco", ver: "50 + 25 = ?", ok: 75, ops: [70,72,75,78] }
            ],
            resta: [
                { voz: "cinco menos dos", ver: "5 - 2 = ?", ok: 3, ops: [1,2,3,4] },
                { voz: "diez menos cuatro", ver: "10 - 4 = ?", ok: 6, ops: [4,5,6,7] },
                { voz: "quince menos siete", ver: "15 - 7 = ?", ok: 8, ops: [6,7,8,9] },
                { voz: "veinte menos cinco", ver: "20 - 5 = ?", ok: 15, ops: [12,14,15,16] },
                { voz: "treinta menos diez", ver: "30 - 10 = ?", ok: 20, ops: [15,18,20,22] },
                { voz: "veintiocho menos ocho", ver: "28 - 8 = ?", ok: 20, ops: [18,19,20,21] },
                { voz: "cincuenta menos veinte", ver: "50 - 20 = ?", ok: 30, ops: [25,28,30,32] },
                { voz: "cuarenta y cinco menos quince", ver: "45 - 15 = ?", ok: 30, ops: [28,29,30,31] },
                { voz: "sesenta menos veinticinco", ver: "60 - 25 = ?", ok: 35, ops: [32,34,35,36] },
                { voz: "cien menos cincuenta", ver: "100 - 50 = ?", ok: 50, ops: [40,45,50,55] }
            ],
            multiplicacion: [
                { voz: "dos por tres", ver: "2 × 3 = ?", ok: 6, ops: [5,6,7,8] },
                { voz: "cinco por cuatro", ver: "5 × 4 = ?", ok: 20, ops: [15,18,20,24] },
                { voz: "tres por seis", ver: "3 × 6 = ?", ok: 18, ops: [16,17,18,19] },
                { voz: "siete por dos", ver: "7 × 2 = ?", ok: 14, ops: [12,13,14,15] },
                { voz: "cuatro por cinco", ver: "4 × 5 = ?", ok: 20, ops: [18,20,22,25] },
                { voz: "seis por tres", ver: "6 × 3 = ?", ok: 18, ops: [15,18,21,24] },
                { voz: "ocho por dos", ver: "8 × 2 = ?", ok: 16, ops: [14,15,16,17] },
                { voz: "diez por cinco", ver: "10 × 5 = ?", ok: 50, ops: [40,45,50,55] },
                { voz: "tres por diez", ver: "3 × 10 = ?", ok: 30, ops: [25,28,30,32] },
                { voz: "cinco por cinco", ver: "5 × 5 = ?", ok: 25, ops: [20,22,25,30] }
            ],
            division: [
                { voz: "seis entre dos", ver: "6 ÷ 2 = ?", ok: 3, ops: [2,3,4,5] },
                { voz: "diez entre cinco", ver: "10 ÷ 5 = ?", ok: 2, ops: [1,2,3,4] },
                { voz: "doce entre tres", ver: "12 ÷ 3 = ?", ok: 4, ops: [2,3,4,6] },
                { voz: "veinte entre cuatro", ver: "20 ÷ 4 = ?", ok: 5, ops: [4,5,6,8] },
                { voz: "treinta entre diez", ver: "30 ÷ 10 = ?", ok: 3, ops: [2,3,5,6] },
                { voz: "veinticuatro entre seis", ver: "24 ÷ 6 = ?", ok: 4, ops: [3,4,6,8] },
                { voz: "cincuenta entre cinco", ver: "50 ÷ 5 = ?", ok: 10, ops: [8,9,10,12] },
                { voz: "cuarenta entre ocho", ver: "40 ÷ 8 = ?", ok: 5, ops: [4,5,7,8] },
                { voz: "sesenta entre diez", ver: "60 ÷ 10 = ?", ok: 6, ops: [5,6,8,10] },
                { voz: "cien entre diez", ver: "100 ÷ 10 = ?", ok: 10, ops: [8,9,10,15] }
            ]
        };

        let operacionActual = "";
        let indice = 0;
        let vozLista = false;

        // FUNCIÓN DE VOZ
        function hablar(texto) {
            if(!vozLista) return;
            window.speechSynthesis.cancel();
            const voz = new SpeechSynthesisUtterance(texto);
            voz.lang = "es-ES";
            voz.rate = 0.9;
            setTimeout(()=> window.speechSynthesis.speak(voz), 200);
        }

        function activarVoz() {
            vozLista = true;
            document.getElementById('activarSonido').style.display = 'none';
            document.getElementById('btnLeer').style.display = 'inline-block';
            hablar("Sonido activado.");
        }

        function leer() {
            if(vozLista) hablar(bancos[operacionActual][indice].voz);
        }

        // CAMBIAR DE OPERACIÓN
        function cargarOperacion(tipo) {
            operacionActual = tipo;
            indice = 0;
            vozLista = false;
            document.getElementById('menu').style.display = 'none';
            document.getElementById('ejercicios').style.display = 'block';
            document.getElementById('tituloOperacion').textContent = tipo.toUpperCase();
            document.getElementById('activarSonido').style.display = 'block';
            document.getElementById('btnLeer').style.display = 'none';
            cargarEjercicio();
        }

        function volverMenu() {
            document.getElementById('ejercicios').style.display = 'none';
            document.getElementById('menu').style.display = 'block';
        }

        // CARGAR EJERCICIO
        function cargarEjercicio() {
            const e = bancos[operacionActual][indice];
            document.getElementById('textoEjercicio').textContent = e.ver;
            const botones = document.querySelectorAll('.opcion');
            botones.forEach((b,i)=>{
                b.textContent = e.ops[i];
                b.className = 'opcion';
                b.disabled = false;
            });
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
            if(vozLista) hablar(e.voz);
        }

        // VERIFICAR RESPUESTA
        function verificar(boton, valor) {
            if(!vozLista){ alert("Primero activa el sonido"); return; }
            const ok = bancos[operacionActual][indice].ok;
            document.querySelectorAll('.opcion').forEach(b=>b.disabled=true);

            if(parseInt(boton.textContent) === ok){
                boton.classList.add('correcta');
                const m = "¡Muy bien! Respuesta correcta";
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }else{
                boton.classList.add('incorrecta');
                document.querySelectorAll('.opcion').forEach(b=>{
                    if(parseInt(b.textContent) === ok) b.classList.add('correcta');
                });
                const m = `No es esa. La correcta es ${ok}`;
                document.getElementById('mensaje').textContent = m;
                hablar(m);
            }
            document.getElementById('siguiente').style.display = 'block';
            window.scrollTo(0, document.body.scrollHeight);
        }

        // SIGUIENTE EJERCICIO
        function siguienteEjercicio() {
            indice = (indice + 1) % bancos[operacionActual].length;
            cargarEjercicio();
        }
    </script>
</body>
</html>
