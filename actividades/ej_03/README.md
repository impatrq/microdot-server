# ej_03

## Consigna

Implementar dentro de la etiqueta `main` una barra o slider que me permita elegir una temperatura de setpoint entre 0 y 30 grados. El valor indicado por el slider debe enviarse, al soltarlo, al servidor para actualizar la referencia.

En la página, debe verse también un campo en donde se indica la temperatura indicada por el sensor de la placa de desarrollo. Se tendrá que pedir periódicamente (`setInterval` en JavaScript).

Cuando la temperatura real supere la indicada por el slider, en la placa de desarrollo debe activarse el buzzer.

Periódicamente debe refrescarse una etiqueta en la página que indique el estado del buzzer.

Los datos en el `header` y `footer` deben completarse según corresponda.