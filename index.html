<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ejercicios de Sumas - Elige la respuesta</title>
    <style>
        body { font-family: Arial; max-width: 500px; margin: 3rem auto; padding: 0 1rem; }
        .caja { background: #f5f5f5; padding: 2rem; border-radius: 10px; text-align: center; }
        .operacion { font-size: 2rem; font-weight: bold; margin: 1.5rem 0; color: #1e40af; }
        .opcion { display: block; width: 100%; padding: 0.9rem; margin: 0.6rem 0; font-size: 1.1rem; border: 2px solid #ccc; border-radius: 8px; cursor: pointer; background: white; transition: 0.2s; }
        .opcion:hover { border-color: #2563eb; background: #eff6ff; }
        .correcta { border-color: #16a34a; background: #dcfce7; color: #166534; font-weight: bold; }
        .incorrecta { border-color: #dc2626; background: #fee2e2; color: #991b1b; }
        #mensaje { margin-top: 1.5rem; font-size: 1.3rem; font-weight: bold; }
        #siguiente { margin-top: 1rem; background: #2563eb; color: white; border: none; padding: 0.8rem 1.5rem; border-radius: 5px; cursor: pointer; display: none; }
    </style>
</head>
<body>
    <div class="caja">
        <h2>¿Cuál es el resultado?</h2>
        <div class="operacion" id="operacion">5 + 3 = ?</div>

        <button class="opcion" onclick="verificar(this, 7)">7</button>
        <button class="opcion" onclick="verificar(this, 8)">8</button>
        <button class="opcion" onclick="verificar(this, 9)">9</button>
        <button class="opcion" onclick="verificar(this, 10)">10</button>

        <div id="mensaje"></div>
        <button id="siguiente" onclick="cambiarEjercicio()">Siguiente ejercicio</button>
    </div>

    <script>
        // Lista de ejercicios ya definidos
        const ejercicios = [
            { suma: "5 + 3 = ?", correcta: 8, opciones: [7,8,9,10] },
            { suma: "12 + 4 = ?", correcta: 16, opciones: [14,15,16,17] },
            { suma: "20 + 5 = ?", correcta: 25, opciones: [22,24,25,27] },
            { suma: "8 + 9 = ?", correcta: 17, opciones: [15,16,17,18] }
        ];

        let actual = 0;

        function cargarEjercicio() {
            const e = ejercicios[actual];
            document.getElementById('operacion').textContent = e.suma;
            const botones = document.querySelectorAll('.opcion');
            botones.forEach((btn, i) => {
                btn.textContent = e.opciones[i];
                btn.className = 'opcion';
                btn.disabled = false;
            });
            document.getElementById('mensaje').textContent = '';
            document.getElementById('siguiente').style.display = 'none';
        }

        function verificar(boton, valorElegido) {
            const correcta = ejercicios[actual].correcta;
            // Bloquear todas las opciones al elegir una
            document.querySelectorAll('.opcion').forEach(b => b.disabled = true);

            if (valorElegido === correcta) {
                boton.classList.add('correcta');
                document.getElementById('mensaje').textContent = '✅ ¡MUY BIEN! Es la respuesta correcta';
            } else {
                boton.classList.add('incorrecta');
                // Resaltar la correcta
                document.querySelectorAll('.opcion').forEach(b => {
                    if (parseInt(b.textContent) === correcta) b.classList.add('correcta');
                });
                document.getElementById('mensaje').textContent = '❌ Inténtalo de nuevo. La correcta está marcada';
            }

            // Mostrar botón para seguir
            document.getElementById('siguiente').style.display = 'inline-block';
        }

        function cambiarEjercicio() {
            actual = (actual + 1) % ejercicios.length;
            cargarEjercicio();
        }

        // Cargar el primer ejercicio al abrir
        cargarEjercicio();
    </script>
</body>
</html>
