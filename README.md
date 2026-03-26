# Core-Dump: System Recovery

**Core-Dump: System Recovery** es un videojuego de aventura y gestión de recursos desarrollado en **Python** bajo el paradigma de **Programación Orientada a Objetos (POO)**. El juego simula un entorno técnico donde el usuario debe restaurar la estabilidad de un sistema computacional dañado.

## Descripción del Proyecto
El jugador asume el rol de un administrador de sistemas que debe navegar por nodos críticos, recolectar recursos económicos (**Bits**) y gestionar su **Energía** e **Integridad** para sobrevivir. El objetivo final es fortalecerse mediante la compra de ítems para derrotar a la amenaza principal: el `GIGA_VIRUS`.

## Conceptos de Programación Aplicados
Este proyecto sirve como implementación práctica de los pilares de la POO:

* **Abstracción:** Uso de la clase base `GameObject` y la clase `Actor` para definir comportamientos generales de entidades vivas y objetos pasivos.
* **Herencia:** Estructura jerárquica donde `Player` y `Boss` heredan de `Actor`, compartiendo lógica de supervivencia.
* **Encapsulamiento:** Protección de atributos sensibles como `__potencia` y `__precio` en la clase `Item`, accesibles solo mediante propiedades.
* **Polimorfismo:** Implementación del método abstracto `obtener_reporte()`, el cual devuelve una visualización distinta dependiendo de si la entidad es un Jugador, un Ítem o un Jefe.

## Mecánicas de Juego
1.  **Exploración:** Gasta energía para encontrar Bits. Existe un riesgo de error que daña la integridad del sistema del jugador.
2.  **Reparación de Sectores:** Permite avanzar en la jerarquía del sistema (Kernel, Firewall) utilizando ítems de potencia adecuada.
3.  **Tienda (Shop):** Interfaz para intercambiar Bits por "Parches" de alta potencia necesarios para el combate final.
4.  **Gestión Vital:** Mecánica de intercambio donde el jugador puede sacrificar vida para obtener energía y evitar el apagado del sistema.
5.  **Batalla Final:** Enfrentamiento táctico contra el Boss utilizando los objetos recolectados en la mochila.

## Instalación y Ejecución
Para ejecutar el juego en su entorno local:

1.  Asegúrese de tener instalado **Python 3.10** o superior.
2.  Descargue el archivo `sS.py` (o el nombre que haya asignado al archivo).
3.  Ejecute el script desde su terminal o IDE (PyCharm):
    ```bash
    python sS.py
    ```


## 👥 Equipo de Desarrollo =)
* **Samuel Marroquín**
* **María Camila Pradilla**
* **John Gallego Zambrano**

----
*Proyecto académico para el curso de Programación Orientada a Objetos - Universidad de Medellín (2026-1).*