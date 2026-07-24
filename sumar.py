<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicios de Sumas - Con voz</title>
    <style>
        body { font-family: Arial; max-width: 550px; margin: 3rem auto; padding: 0 1rem; }
        .caja { background: #f0f9ff; padding: 2rem; border-radius: 12px; text-align: center; border: 2px solid #0369a1; }
        .operacion { font-size: 2.2rem; font-weight: bold; margin: 1.5rem 0; color: #0c4a6e; }
        .opcion { display: inline-block; width: 45%; padding: 1rem; margin: 0.5rem 2%; font-size: 1.3rem; border: 2px solid #94a3b8; border-radius: 8px; cursor: pointer; background: white; transition: 0.2s; }
        .opcion:hover { border-color: #0284c7; background: #e0f2fe; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #ef4444; background: #fee2e2; color: #b91c1c; }
        #mensaje { margin-top: 1.5rem; font-size: 1.4rem; font-weight: bold; }
        #siguiente { margin-top: 1.2rem; background: #2563eb; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 8px; cursor: pointer; display: none; font-size: 1rem; }
        #btnVoz { background: #f59e0b; color: white; border: none; padding: 0.6rem 1.2rem; border-radius: 8px; cursor: pointer; margin-bottom: 1rem; font-size: 1rem; }
    </style>
</head>
<body>
    <div class="caja">
        <h2>¿Cuál es el resultado?</h2>
        <button id="btnVoz" onclick="leerSuma()">🔊 Escuchar la suma</button>
        <div class="operacion" id="mostrarSuma">7 + 5 = ?</div>

        <button class="opcion" onclick="comprobar(this, 11)">11</button>
        <button class="opcion" onclick="comprobar(this, 12)">12</button>
        <button class="opcion" onclick="comprobar(this, 13)">13</button>
        <button class="opcion" onclick="comprobar(this, 14)">14</button>

        <div id="mensaje"></div>
        <button id="siguiente" onclick="cambiarEjercicio()">Siguiente suma</button>
    </div>

    <script>
        const ejercicios = [
            { suma: "7 más 5", texto: "7 + 5 = ?", respuestaBuena: 12, opciones: [11, 12, 13, 14] },
            { suma: "15 más 6", texto: "15 + 6 = ?", respuestaBuena: 21, opciones: [19, 20, 21, 22] },
            { suma: "30 más 10", texto: "30 + 10 = ?", respuestaBuena: 40, opciones: [35, 38, 40, 45] },
            { suma: "9 más 8", texto: "9 + 8 = ?", respuestaBuena: 17, opciones: [15, 16, 17, 18] },
            { suma: "24 más 5", texto: "24 + 5 = ?", respuestaBuena: 29, opciones: [27, 28, 29, 30] }
        ];

        let indice = 0;

        function hablar(texto) {
            // Detener cualquier voz anterior
            window.speechSynthesis.cancel();
            const voz = new SpeechSynthesisUtterance(texto);
            voz.lang = "es-ES";
            voz.rate = 0.9; // Velocidad normal
            window.speechSynthesis.speak(voz);
        }

        function leerSuma() {
            hablar(ejercicios[indice].suma);
        }

        function cargarSuma() {
            const dato = ejercicios[indice];
            document.getElementById('mostrarSuma').textContent = dato.texto;
            const botones = document.querySelectorAll('.opcion');
            botones.forEach((btn, pos) => {
                btn.textContent = dato.opciones[pos];
                btn.className = 'opcion';
                btn.disabled = false;
            });
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
            // Lee automáticamente al cambiar de ejercicio
            hablar(`Ejercicio: ${dato.suma}`);
        }

        function comprobar(botonElegido, valor) {
            const correcta = ejercicios[indice].respuestaBuena;
            document.querySelectorAll('.opcion').forEach(b => b.disabled = true);

            if (valor === correcta) {
                botonElegido.classList.add('correcta');
                const mensaje = "¡Muy bien! Respuesta correcta";
                document.getElementById('mensaje').textContent = mensaje;
                hablar(mensaje);
            } else {
                botonElegido.classList.add('incorrecta');
                document.querySelectorAll('.opcion').forEach(b => {
                    if (parseInt(b.textContent) === correcta) b.classList.add('correcta');
                });
                const mensaje = "No es esa. La respuesta correcta es " + correcta;
                document.getElementById('mensaje').textContent = mensaje;
                hablar(mensaje);
            }

            document.getElementById('siguiente').style.display = 'inline-block';
        }

        function cambiarEjercicio() {
            indice = (indice + 1) % ejercicios.length;
            cargarSuma();
        }

        // Iniciar y leer la primera suma
        cargarSuma();
    </script>
</body>
</html>
