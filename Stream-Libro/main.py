<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intro: Una historia fantaciosa de Realidad Anomala</title>
    <style>
        /* RESET BÁSICO Y FONDO MALVAVISCO MATE */
        body, h1, p { margin: 0; padding: 0; }
        body {
            background-color: #FDF7EF;
            background-image: 
                radial-gradient(#FFF1DF 1px, transparent 1px),
                radial-gradient(circle, #FFF1DF 0%, #FDF7EF 100%);
            background-size: 20px 20px, auto;
            background-blend-mode: soft-light;
            box-shadow: inset 0 0 100px rgba(0,0,0,0.03); 
            font-family: 'Garamond', 'Georgia', serif;
            line-height: 1.7;
            display: flex;
            flex-direction: column;
            align-items: center;
            min-height: 100vh;
            padding: 40px;
            box-sizing: border-box;
        }

        .page-content {
            max-width: 700px;
            text-align: center;
            position: relative;
        }

        .page-title {
            position: absolute;
            top: -30px;
            left: 0;
            font-size: 14px;
            color: rgba(0, 45, 114, 0.7);
            font-style: italic;
        }

        h1 {
            color: #002D72;
            font-size: 80px;
            font-weight: normal;
            margin-bottom: 50px;
            letter-spacing: 15px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }

        /* CONTENEDOR DONDE CAERÁ EL STREAM */
        #stream-container {
            width: 100%;
        }

        p {
            color: #002D72; 
            font-size: 20px;
            margin-bottom: 30px;
            font-weight: 300;
            /* EFECTO FADE-IN PARA CUANDO APAREZCA TEXTO NUEVO */
            animation: fadeIn 1s ease-out forwards;
            opacity: 0;
        }

        /* ESTILO PARA LOS EASTER EGGS / IMÁGENES */
        .easter-egg {
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0, 45, 114, 0.15);
            animation: fadeIn 1.2s ease-out forwards;
            opacity: 0;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <div class="page-content">
        <div class="page-title">Libro : Una historia fantaciosa de Realidad Anomala</div>
        
        <h1>INTRO...</h1>

        <div id="stream-container">
            <p>
                Esta es la historia de como Serafin Sandoval Angel paso de el chico que Aguanto golpes de la vida y Llego al punto de lograr sus Sueños, despues de pelear con el universo logro Subir > esto es una historia en tiempo real que se ira Emitiendo en tiempo real donde veras accion, drama, romanse, paranormal, comedia y lo mejor de esto es que te iras comprendiendo > te engancharas, con Su vida tan anormal la historia comienza apartir de... la hoja 1 de Este libro pero empezaremos por 24 años.
            </p>
        </div>
    </div>

    <script>
        // REEMPLAZA ESTA URL CON LA QUE TE DE RENDER O RAILWAY (Ej: tu-app.onrender.com)
        const SERVIDOR_URL = "tu-app.onrender.com"; 
        
        // Conectamos el cable con el servidor
        const ws = new WebSocket(`wss://${SERVIDOR_URL}/stream`);
        const container = document.getElementById('stream-container');

        // Escuchamos los comandos en vivo
        ws.onmessage = function(event) {
            const datos = JSON.parse(event.data);

            // COMANDO 1: ESCRIBIR TEXTO NUEVO
            if (datos.accion === "escribir") {
                const nuevoParrafo = document.createElement('p');
                nuevoParrafo.innerText = datos.texto;
                container.appendChild(nuevoParrafo);
                
                // Auto-scroll suave para que el lector vea lo nuevo abajo
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
            }

            // COMANDO 2: METER EASTER EGG (IMAGEN)
            if (datos.accion === "subir_huevo") {
                const nuevaImagen = document.createElement('img');
                nuevaImagen.src = datos.url;
                nuevaImagen.id = datos.id; // Le asignamos el ID único para poder borrarlo
                nuevaImagen.className = "easter-egg";
                container.appendChild(nuevaImagen);
            }

            // COMANDO 3: DESTRUIR ELEMENTO POR ID (Quitar secretos)
            if (datos.accion === "eliminar") {
                const elementoAbuscar = document.getElementById(datos.id);
                if (elementoAbuscar) {
                    elementoAbuscar.remove(); // Desaparece del código en vivo
                }
            }
        };

        // Si la conexión se cae, intenta reconectar automáticamente cada 5 segundos
        ws.onclose = function() {
            console.log("Conexión perdida. Reconectando...");
            setTimeout(() => { location.reload(); }, 5000);
        };
    </script>

</body>
</html>
