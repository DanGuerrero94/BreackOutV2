# BreackOutV2
Juego Popular "Breack Out / Arkanoid" realizado en Python con Thonny (usando de base install py game zero)

FONDO:
- Aumentada dimension de pantalla a 800x600
- Cambiado background.png por una imagen de tenis de fondo


BLOQUES:
- Reducido tamaño de 64x32 a 32x16
- Se ajustaron las distancias X y Y para acercar aun mas las barras
- Mejoradas las colisiones con la pelota de tenis para parecer mas fluido al golpear
- Se añadieron colores "celeste gris violeta amarillo y naranja" editados con befunky.com (edicion de imagenes)


ENTORNO:
- Modificada pelota a greenball.png
- Se guardaron los archivos originales en la carpeta originales para diferenciar de los actuales
- Velocidad aumentada / paddle.x left de -5 a -6 y paddle.x right de +5 a +6
- Velocidad de la Pelota aumentada / ball_x_speed = de -1 a 3 ; ball_y_speed = de -1 a 3
- Añadido sistema de puntaje:
 . Declarado en def update la variable "score"
 . Definido un texto y la alineacion, se utilizo color verde amarillo =(173,255,47)
 . Establecido fontsize = 25
- Seteado un lvl_win cuando la pelota termina con todas las barras
 Total: 16 x 8 bloques = 128 -- Al llegar el score en 128, saldra un mensaje en pantalla con el puntaje obtenido
NOTA: para evitar esperar los 128 y corroborar que funciona, modificar score >= 128
NOTA 2: para ver el game over editar ball.y >= 580

update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            bars_list.remove(bar)
            ball_y_speed *= -1
            score = score + 1
        if score >= 128:--------------------#cambiar 128 por otro numero y listo
            lvl_win = True
            ball_x_speed = 0
            ball_y_speed = 0
        if ball.y >= 580:-------------------#cambiar 580 por 300 o otro numero y listo
            game_over = True
            ball_x_speed = 0
            ball_y_speed = 0
    


BARRA:
- Modificado aspecto paddlebar a uno mas agradable
- Editada con befunky.com, y llevada al tamaño la imagen png a 105 x 24
- Añadidas colisiones laterales (izquierda y derecha):

    if (paddle.x <=60):          --- si la barra es igual o menor a 60 no pasara de 60
        paddle.x = 60
    if (paddle.x >=740):         --- si la barra es igual o mayor a 740 no pasara de 740
        paddle.x = 740

. Verticalmente nunca se movera, ya que esta definida la barra en paddle.x = 120 / paddle.y = 560 y las keyboard me garantizan moverlo con la variable "paddle.x" de derecha a izquierda solamente.   Si quisiera moverlo usaria la variable "paddle.y", pero no nos aporta nada el modificar la variable







VIDEOS Y CODIGOS USADOS DE REFERENCIA:
Arkanoid/Breakout Clone in PyGame               (ARCHIVO BASE ORIGINAL)
https://www.youtube.com/watch?v=TQIBDCH0bEI

Simple Arkanoid Game using Python
https://www.youtube.com/watch?v=axnuSkmdywg
https://new.pythonforengineers.com/blog/your-first-game-in-python-in-less-than-30-minutes/

Programando con Pgzero (variante beginner del pygame)
https://quirkycort.github.io/tutorials/20-Pygame-Zero-Basics/20-Gem/50-score.html

Manual de pygame-zero
https://pygame-zero.readthedocs.io/en/stable/








--------------------------------------------- NO LOGRADO AUN (ADICIONALES) ---------------------------------
1. Crear pantalla de inicio y salida. Al dar inicio empezamos a jugar y salida se sale del juego
(se puede en pygame, pero como la estructura es pgzero, hay que adarptarlo y hacer que funcione, inclusive hay un ejemplo usando root.definicion y canvas (literalmente dibuja todo el juego como si fuera paint), pero es mas complicada la sintaxis y mucho mas extensa)

2. Crear bloques de dureza (es necesario golpearlos 2 hasta 3 veces para romperlos)

3. Crear bloques permanentes (block_list y al definir los bloques en teoria deberian volverse indestructibles)

4. Añadir sonidos a los bloques cuando son golpeados, sistema de vidas
NOTA: segun he leido afecta la variable "import" y se crea un sound.py donde se cargan los sonidos y en el codigo del main.py se utilizan
NOTA 2: hay codigos en pygame no en pyzero, sobre el sistema de vida
