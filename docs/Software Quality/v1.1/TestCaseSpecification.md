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
      <b>Datos de Prueba:</b> a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z<br>
      <b>Resultado Esperado:</b> Cada letra del abecedario se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Abecedario Completo en Mayúsculas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de todas las letras del abecedario en mayúscula.<br>
      <b>Datos de Prueba:</b> A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z<br>
      <b>Resultado Esperado:</b> Cada letra del abecedario se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>3</td>
    <td>
      <b>Vocales Acentuadas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de vocales acentuadas.<br>
      <b>Datos de Prueba:</b> 'á', 'é', 'í', 'ó', 'ú'<br>
      <b>Resultado Esperado:</b> Cada vocal acentuada se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>4</td>
    <td>
      <b>Letras especiales Ñ y Ü</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de las letras 'ñ' y 'Ü'.<br>
      <b>Datos de Prueba:</b> 'ñ', 'Ü'<br>
      <b>Resultado Esperado:</b> Cada carácter se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>5</td>
    <td>
      <b>Signos básicos</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de los signos básicos.<br>
      <b>Datos de Prueba:</b> ',', '.', ';', ':', '!', '?', '@', '%', '&', '*', '+', '=', '-', '¡', '¿'<br>
      <b>Resultado Esperado:</b> Cada carácter especial se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>4</td>
    <td>
      <b>Números de una cifra</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de números de una cifra.<br>
      <b>Datos de Prueba:</b> '0' a '9'<br>
      <b>Resultado Esperado:</b> Cada número se traduce a su correspondiente carácter en Braille. No se arrojan errores.
    </td>
  </tr>
   <tr>
    <td>1</td>
    <td>
      <b>Cantidades de Dos o Más Cifras</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades de dos o más cifras, colocando el signo de número solamente al principio.<br>
      <b>Datos de Prueba:</b> '123'<br>
      <b>Resultado Esperado:</b> El texto '123' se traduce a '⠼⠁⠃⠉'. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>2</td>
    <td>
      <b>Cantidades con Puntos</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades que incluyen puntos.<br>
      <b>Datos de Prueba:</b> '1.23'<br>
      <b>Resultado Esperado:</b> El texto '1.23' se traduce a '⠼⠁⠲⠃⠉'. No se arrojan errores.
    </td>
  </tr>
  <tr>
    <td>3</td>
    <td>
      <b>Cantidades con Comas</b><br>
      <b>Descripción:</b> Verificar la traducción correcta de cantidades que incluyen comas.<br>
      <b>Datos de Prueba:</b> '1,23'<br>
      <b>Resultado Esperado:</b> El texto '1,23' se traduce a '⠼⠁⠂⠃⠉'. No se arrojan errores.
    </td>
  </tr>
  
</table>

