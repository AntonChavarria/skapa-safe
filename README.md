# SkapaSafe

<div id="top"></div>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->




<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AntonChavarria/skapa-safe">
    <img src="ss.PNG" alt="Logo" width="150" height="150">
  </a>

  <h3 align="center">Skapa Safe</h3>

  <p align="center">
    Sistema de seguridad automatizado basado en sensores
    <br />
  </p>
</div>




<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

El sistema IoT propuesto es una solución que garantice que todas las ventas de alcohol a menores de edad no se permitan dejando inaccesible la zona donde se encuentran las botellas de alcohol y solamente pudiendo acceder mediante el sistema IoT que nosotros proponemos que estará solamente al alcance de los trabajadores. 

El sistema incorpora las siguientes tecnologias
* Apertura y desbloqueo de puerta mediante un sensor de gestos
* Indicadores led y sonoros sel estado del bloqueo de la puerta
* Sistema de aviso sonoro para casos de robo



<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Empezando

A continuacion se explican los requisitos y procedieminto a seguir para la instalacion y inicio del sistema Skapa Safe

### Prerequisitos

Para el correcto funcionamiento del sistema, en necesario tener instalado Python 3.1
* python
```
 sudo apt-get install python
  ```
  
 Ademas, sera necesario que todos los elementos que vamos a utilizar para la practica esten conectados al puerto correspondiente de su computadora, atendiendo a la siguiente manera:
 - Port 24: BUZZER
 - Port 26: LED Rojo
 - Port I2C: Pantalla LCD
 - Port I2C: Sensor de GESTOS
  
  
### Instalacion

Para el incio del sistema, sera necesario seguir los siguientes pasos

1. Clonar este repositorio
   ```
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Cambiar al directorio creado SkafaSafe
   ```
   cd SkapaSafe
   ```
4. Cambiar directorio dentro de grove.py
   ```
   cd grove.py
   ```
5. Ejecutar el programa
   ```
   python main.py
   ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usabilidad

El sistema desarrollado, ante los estimulos que el usuario ejecute frente a el sensor de gestos, se comportara de la siguiente manera:

_Mediante un giro de muñeca hacia las agujas del reloj, se encienden los dispositivos LED y buzzer (durante 6 segundos) avisando que la puerta esta abierta_<br><br>
_Mediante un giro de muñeca hacia abajo, se activara el buzzer alertando de un supuesto robo_<br><br>
_Mediante un giro de muñeca en contra de las agujas del reloj, se desactivara la alerta por robo, apagando el sonido del buzzer._<br><br>
_Mediante un giro de muñeca hacia la derecha, se almacenan estadísticas de cada uno de los movimientos._<br><br>


<!-- LICENSE -->
## Licencia

Para asegurar la originalidad del codigo este proyecto esta creado bajo licencia. Ver `LICENSE` para mas informacion.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Para cualquier cuestion, duda o peticion de cambios pueden contactar con nosotros por los siguientes enlaces
<br><br>
Skapa Safe - [@skapaSafe](https://twitter.com/skapaSafe) - skapaSafel@gmail.com
<br>
Link de proyecto: [https://github.com/AntonChavarria/skapa-safe](https://github.com/AntonChavarria/skapa-safe)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Dedicacion y creditos

Enlaces directos ha los creadores del proyecto.

* [Anton Chavarria](https://github.com/AntonChavarria)
* [Jagoba Gomez](https://github.com/jagobajr)
* [Aitor Cavia](https://github.com/aitorcavia)


<p align="right">(<a href="#top">back to top</a>)</p>

