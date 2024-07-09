<!-- Historia 1 -->

<h2>Especificación de casos de prueba</h2>

<h3>Historia de Usuario Asociada</h3>
<p><b>No: 1</b> - Transcribir textos de español a braille</p>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que la función de traducción a Braille reconozca y traduzca correctamente varios tipos de caracteres.</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>
      <b>Abecedario Completo en minúsculas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de todas las letras del abecedario en minúscula.<br>
      <b>Datos de Prueba:</b> abcdefghijklmnopqrstuvwxyz<br>
      <b>Resultado Esperado:</b> Cada letra del abecedario se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵
      </div>
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Abecedario Completo en Mayúsculas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de todas las letras del abecedario en mayúscula.<br>
      <b>Datos de Prueba:</b> ABCDEFGHIJKLMNOPQRSTUVWXYZ<br>
      <b>Resultado Esperado:</b> Cada letra del abecedario se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠨⠁⠨⠃⠨⠉⠨⠙⠨⠑⠨⠋⠨⠛⠨⠓⠨⠊⠨⠚⠨⠅⠨⠇⠨⠍⠨⠝⠨⠕⠨⠏⠨⠟⠨⠗⠨⠎⠨⠞⠨⠥⠨⠧⠨⠺⠨⠭⠨⠽⠨⠵
      </div>
    </td>
  </tr>
  <tr>
    <td>3</td>
    <td>
      <b>Vocales Acentuadas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de vocales acentuadas.<br>
      <b>Datos de Prueba:</b> áéíóú<br>
      <b>Resultado Esperado:</b> Cada vocal acentuada se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠷⠮⠌⠬⠾⠳
      </div>
    </td>
  </tr>
  <tr>
    <td>4</td>
    <td>
      <b>Letras especiales ñ y ü</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de las letras 'ñ' y 'Ü'.<br>
      <b>Datos de Prueba:</b> ñü<br>
      <b>Resultado Esperado:</b> Cada carácter se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠻⠳
      </div>
    </td>
  </tr>
  <tr>
    <td>5</td>
    <td>
      <b>Signos básicos</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de los signos básicos.<br>
      <b>Datos de Prueba:</b> Signos básicos:
       <div>
      .,;:_“”¡!¿?()+*=÷-
      </div>
      <b>Resultado Esperado:</b> Cada carácter especial se traduce a su correspondiente carácter en Braille
      <div>
      ⠄⠂⠆⠒⠤⠦⠦⠖⠖⠢⠢⠣⠜⠖⠔⠶⠲⠤
      </div>
    </td>
  </tr>
  <tr>
    <td>6</td>
    <td>
      <b>Números de una cifra</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de números de una cifra, probar número por número no ingresar todos a la vez<br>
      <b>Datos de Prueba:</b> Números del '0' a '9'<br>
      <b>Resultado Esperado:</b> Cada número se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠼⠚, ⠼⠂, ⠼⠆, ⠼⠒, ⠼⠲, ⠼⠢, ⠼⠖, ⠼⠶, ⠼⠦, ⠼⠔
      </div>
    </td>
  </tr>
   <tr>
    <td>7</td>
    <td>
      <b>Cantidades de Dos o Más Cifras</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades de dos o más cifras, el signo de número solamente debe aparecer al principio.<br>
      <b>Datos de Prueba:</b> 123<br>
      <b>Resultado Esperado:</b> El número se traduce a su correspondiente carácter en Braille.No se arrojan errores.
      <div>
      ⠼⠁⠃⠉
      </div>
    </td>
  </tr>
  <tr>
    <td>8</td>
    <td>
      <b>Números con Punto Decimal</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades que incluyen puntos.<br>
      <b>Datos de Prueba:</b> 1.23<br>
      <b>Resultado Esperado:</b> El número se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠼⠁⠄⠃⠉
      </div>
    </td>
  </tr>
  <tr>
    <td>9</td>
    <td>
      <b>Números con Coma Decimal</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades que incluyen comas.<br>
      <b>Datos de Prueba:</b> '1,23'<br>
      <b>Resultado Esperado:</b> El número se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
      ⠼⠁⠂⠃⠉
      </div>
    </td>
  </tr>
  
</table>

<!--Historia 2-->

<h2>Casos de Prueba para Historia de Usuario 2</h2>

<h3>Historia de Usuario Asociada</h3>
<p><b>No: 2</b> - Transcribir textos de Braille a Español</p>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que la función de transcripción de Braille a Español maneje correctamente letras del abecedario, vocales acentuadas, signos básicos y números.</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>
      <b>Letras minúsculas del Abecedario</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de letras minúsculas del abecedario.<br>
      <b>Datos de Prueba:</b> Letras minúsculas en Braille:
      <div>
        ⠁⠃⠉⠙⠑⠋⠛⠓⠊⠚⠅⠇⠍⠝⠕⠏⠟⠗⠎⠞⠥⠧⠺⠭⠽⠵
      </div>
      <b>Resultado Esperado:</b> Cada letra en Braille se transcribe a su correspondiente letra en español. No se arrojan errores.<br>
      Letras minúsculas esperadas:
      <div>
        abcdefghijklmnopqrstuvwxyz
      </div>
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Letras mayúsculas del Abecedario</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de letras mayúsculas del abecedario.<br>
      <b>Datos de Prueba:</b> Letras mayúsculas en Braille:
      <div>
        ⠨⠁⠨⠃⠨⠉⠨⠙⠨⠑⠨⠋⠨⠛⠨⠓⠨⠊⠨⠚⠨⠅⠨⠇⠨⠍⠨⠝⠨⠕⠨⠏⠨⠟⠨⠗⠨⠎⠨⠞⠨⠥⠨⠧⠨⠺⠨⠭⠨⠽⠨⠵
      </div>
      <b>Resultado Esperado:</b> Cada letra en Braille se transcribe a su correspondiente letra en español. No se arrojan errores.<br>
      Letras mayúsculas esperadas:
      <div>
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
      </div>
    </td>
  </tr>
  <tr>
    <td>3</td>
    <td>
      <b>Vocales Acentuadas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de vocales acentuadas.<br>
      <b>Datos de Prueba:</b> Vocales acentuadas en Braille 'á', 'é', 'í', 'ó', 'ú':
      <div>
        ⠷⠮⠌⠬⠾
      </div>
      <b>Resultado Esperado:</b> Cada vocal acentuada en Braille se transcribe a su correspondiente vocal en español. No se arrojan errores.<br>
      Vocales acentuadas esperadas:
      <div>
        áéíóú
      </div>
    </td>
  </tr>
  <tr>
    <td>4</td>
    <td>
      <b>Letras especiales ñ y ü</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de letras especiales'.<br>
      <b>Datos de Prueba:</b> Letras especiales en Braille'ñ', 'ü':
      <div>
        ⠻⠳
      </div>
      <b>Resultado Esperado:</b> Cada carácter se traduce a su correspondiente carácter en Braille. No se arrojan errores.
      <div>
        ñü
      </div>
    </td>
  </tr>
  <tr>
    <td>5</td>
    <td>
      <b>Signos básicos</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de los signos básicos.<br>
      <b>Datos de Prueba:</b>Signos básicos en Braille '.', ',', ';', ':', '_', '“', '”', '¡', '!', '¿', '?', '(', ')', '+', '*', '=', '÷', '-':<br>
      <div>
        ⠄⠂⠆⠒⠤⠦⠦⠖⠖⠢⠢⠣⠜⠖⠔⠶⠲⠤
      </div>
      <b>Resultado Esperado:</b> Cada carácter especial se traduce a su correspondiente carácter en Braille. No se arrojan errores.<br>
      <div>
        <b>Signos esperados:</b> .,;:_“”¡!¿?()+*=÷-
      </div>
    </td>
</tr>
  <tr>
    <td>6</td>
    <td>
      <b>Números de una cifra</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de números de una cifra, probar número por número no ingresar todos a la vez<br>
      <b>Datos de Prueba:</b>Números de una cifra en Braille '0' al '9':
      <div>
        ⠼⠁ ⠼⠃ ⠼⠉ ⠼⠙ ⠼⠑ ⠼⠋ ⠼⠛ ⠼⠓ ⠼⠊ ⠼⠚
      </div>
      <b>Resultado Esperado:</b> Cada número en Braille se transcribe a su correspondiente número en español. No se arrojan errores.<br>
      Números esperados:
      <div>
        0 1 2 3 4 5 6 7 8 9
      </div>
    </td>
  </tr>

  <tr>
    <td>7</td>
    <td>
      <b>Números de Dos o Más Cifras</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de números de dos o más cifras.<br>
      <b>Datos de Prueba:</b> Número de dos cifras en Braille 12:
      <div>
        ⠼⠁⠃ 
      </div>
      <b>Resultado Esperado:</b>
      <div>
        12
      </div>
    </td>
</tr>
<tr>
    <td>8</td>
    <td>
      <b>Números con Punto Decimal</b><br>
      <b>Descripción:</b> Verificar la trducción correcta de números con punto decimal.<br>
      <b>Datos de Prueba:</b> Número con punto decimal en Braille 1.2:
      <div>
        ⠼⠁⠄⠃
      </div>
      <b>Resultado Esperado:</b> 
      <div>
        1.2 
      </div>
    </td>
</tr>
<tr>
    <td>9</td>
    <td>
      <b>Números con Coma Decimal</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de números con coma decimal.<br>
      <b>Datos de Prueba:</b> Número con coma decimal en Braille 2,3:
      <div>
        ⠼⠃⠂⠉ 
      </div>
      <b>Resultado Esperado:</b>
      <div>
        2,3
      </div>
    </td>
</tr>

</table>

<!--Historia 3-->

<h3>Casos de Prueba para Historia de Usuario 3</h3>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que la función de generación de señalética en braille a partir de textos en español permita guardar la imagen generada cuando se presiona el botón "Generar impresión en Espejo".</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>
      <b>Guardar Señalética Generada</b><br>
      <b>Descripción:</b> Verificar que la imagen de señalética generada en braille se guarde correctamente cuando se presiona el botón "Generar impresión en Espejo".<br>
      <b>Datos de Prueba:</b> Texto en español: "Peligro"<br>
      <b>Pasos:</b>
      <ol>
        <li>Ingresar el texto "Peligro" en la aplicación.</li>
        <li>Generar la señalética en braille.</li>
        <li>Presionar el botón "Generar impresión en Espejo".</li>
        <li>Seleccionar la ubicación para guardar el archivo.</li>
      </ol>
      <b>Resultado Esperado:</b> La señalética en braille generada se guarda correctamente en la ubicación seleccionada sin errores.
    </td>
  </tr>
</table>

<!--Historia 4-->
<h3>Casos de Prueba para Historia de Usuario 4</h3>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que la función de generación de impresiones en espejo de textos Braille permita guardar la imagen generada cuando se presiona el botón "Generar impresión en Espejo".</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Verificar Contenido de la Imagen Generada</b><br>
      <b>Descripción:</b> Verificar que la imagen de señalética generada contiene correctamente el texto en braille en espejo correspondiente al texto ingresado.<br>
      <b>Datos de Prueba:</b> Texto en español: "Hola"<br>
      <b>Pasos:</b>
      <ol>
        <li>Ingresar el texto "Hola" en la aplicación.</li>
        <li>Presionar el botón "Español a Braille"</li>
        <li>Presionar el botón "Generar impresión en Espejo".</li>
        <li>Guardar la imagen generada en la computadora.</li>
        <li>Abrir la imagen guardada y verificar visualmente que el texto en braille corresponde correctamente al texto ingresado.</li>
      </ol>
      <b>Resultado Esperado:</b> La imagen guardada muestra correctamente el texto "⠨⠓⠕⠇⠁" en braille sin errores.
    </td>
  </tr>
</table>
<br>
<br>
<!--Especifición de casos de prueba de características no funcionales-->

<!--Compatibilidad: Coexistencia-->

<h3>Casos de Prueba para Historia de Usuario 5</h3>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que la aplicación pueda coexistir con otros programas en ejecución sin generar conflictos, y monitorear el uso de recursos para asegurar un rendimiento eficiente.</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>
      <b>Pruebas en Diferentes Entornos y Monitoreo de Recursos</b><br>
      <b>Descripción:</b> Verificar que la aplicación funcione correctamente en diferentes entornos con otros programas en ejecución, utilizando la librería <code>psutil</code> para monitorear el uso de CPU y memoria.<br>
      <b>Datos de Prueba:</b> 
      <ul>
        <li>Entorno 1: Windows 10 con Google Chrome, Microsoft Word y Spotify en ejecución.</li>
        <li>Entorno 2: macOS Catalina con Safari, Pages y iTunes en ejecución.</li>
        <li>Entorno 3: Windows 11 con Fornite, VLC Media Player y Photoshop en ejecución.</li>
      </ul>F
      <b>Pasos:</b>
      <ol>
        <li>Ejecutar la aplicación en el entorno de prueba especificado.</li>
        <li>Ejecutar simultáneamente los otros programas mencionados para el entorno de prueba.</li>
        <li>Utilizar la librería <code>psutil</code> para monitorear el uso de CPU y memoria.</li>
        <li>Observar el comportamiento de la aplicación y de los otros programas, detectando cualquier conflicto o interferencia.</li>
        <li>Documentar cualquier incidencia observada y el uso de recursos durante la prueba.</li>
        <li>Repetir los pasos anteriores para cada uno de los entornos de prueba especificados.</li>
      </ol>
      <b>Resultado Esperado:</b> La aplicación y los otros programas coexisten sin conflictos ni interferencias, y el uso de recursos por la aplicación es eficiente y estable en cada uno de los entornos de prueba especificados.
    </td>
  </tr>
</table>

<!--Capacidad: Aprendizabilidad-->

<h3>Casos de Prueba para Historia de Usuario 6</h3>

<h3>Objetivo de la Prueba</h3>
<p>Verificar que el manual de usuario en PDF esté disponible, sea accesible y efectivamente ayude a los usuarios a aprender a usar la aplicación.</p>

<h3>Casos de Prueba</h3>

<table>
  <tr>
    <th>No:</th>
    <th>Descripción del Caso de Prueba</th>
  </tr>
  <tr>
    <td>1</td>
    <td>
      <b>Disponibilidad del Manual</b><br>
      <b>Descripción:</b> Verificar que el manual de usuario en PDF esté disponible para descargar desde la sección de ayuda.<br>
      <b>Datos de Prueba:</b> Acceso a la sección de ayuda desde la aplicación.<br>
      <b>Pasos:</b>
      <ol>
        <li>Acceder a la aplicación e ir a la sección de ayuda.</li>
        <li>Buscar la opción para descargar el manual de usuario en PDF.</li>
        <li>Descargar el manual y verificar que el archivo se descarga correctamente.</li>
      </ol>
      <b>Resultado Esperado:</b> El manual de usuario en PDF está disponible y se descarga correctamente desde la sección de ayuda.
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Contenido del Manual</b><br>
      <b>Descripción:</b> Verificar que el contenido del manual de usuario en PDF explique detalladamente cómo utilizar las funcionalidades de la aplicación.<br>
      <b>Datos de Prueba:</b> Manual de usuario en PDF.<br>
      <b>Pasos:</b>
      <ol>
        <li>Abrir el manual de usuario en PDF.</li>
        <li>Leer el contenido del manual, revisando las secciones que explican las funcionalidades de la aplicación.</li>
        <li>Verificar que las explicaciones sean claras, detalladas y fáciles de entender.</li>
      </ol>
      <b>Resultado Esperado:</b> El manual de usuario en PDF proporciona explicaciones claras sobre cómo utilizar las funcionalidades de la aplicación.
    </td>
  </tr>
</table>



