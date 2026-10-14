# Bitácora de uso de inteligencia artificial

## 1. Objetivo del uso de IA

Se utilizó inteligencia artificial como herramienta de apoyo para desarrollar una aplicación de programación funcional en Python con interfaz gráfica.

El objetivo fue facilitar la organización del proyecto, comprender los conceptos estudiados en clase y revisar las decisiones técnicas durante la implementación.

## 2. Prompts utilizados

### Prompt 1: Diseño del proyecto

Se solicitó ayuda para interpretar la guía de la actividad integradora y proponer una aplicación que permitiera aplicar los conceptos de las unidades 1 y 2.

**Resultado:** se propuso desarrollar un simulador de arena de combate.

### Prompt 2: Modelado de datos

Se solicitó ayuda para definir las estructuras que representan al jugador y a los enemigos utilizando `dataclass` y anotaciones de tipos.

**Resultado:** se implementaron las estructuras `Personaje` y `Enemigo`, utilizando `frozen=True` para impedir la modificación directa de sus atributos.

### Prompt 3: Implementación de la lógica

Se solicitó orientación para implementar funciones puras, pattern matching, closures, expresiones lambda, inmutabilidad y herramientas funcionales.

**Resultado:** se creó un módulo de lógica independiente de la interfaz gráfica.

### Prompt 4: Interfaz gráfica

Se solicitó ayuda para construir una interfaz con Tkinter y Ttk-Bootstrap.

**Resultado:** se implementó una ventana con indicadores de vida, selección de enemigos, botones de combate, historial y estadísticas.

### Prompt 5: Documentación

Se solicitó ayuda para organizar el análisis funcional y registrar el uso de inteligencia artificial durante el desarrollo.

**Resultado:** se prepararon los documentos correspondientes para explicar los conceptos utilizados.

## 3. Fragmentos sugeridos por la IA

Entre los elementos sugeridos se encuentran:

- Las estructuras `Personaje` y `Enemigo`.
- La función `crear_multiplicador()` para demostrar un closure.
- La función `procesar_accion()` para aplicar `match/case`.
- El uso de `map()`, `filter()` y `reduce()`.
- La separación del proyecto en módulos.
- La interfaz gráfica desarrollada con Tkinter y Ttk-Bootstrap.

## 4. Qué se aceptó

Se aceptó la propuesta de desarrollar un simulador de combate porque permite representar situaciones concretas y aplicar los conceptos de programación funcional.

También se aceptaron la separación de los archivos, el modelado mediante `dataclass`, el uso de funciones independientes para la lógica y la creación de una interfaz gráfica.

## 5. Qué se modificó o revisó

Se ejecutó la aplicación para comprobar que se abriera correctamente y que sus controles principales respondieran a las acciones del usuario.

Además, se identificó la necesidad de revisar las recompensas de experiencia, las estadísticas y la consistencia entre las distintas formas de atacar.

La revisión de estos aspectos es importante porque una aplicación puede ejecutarse correctamente y, aun así, presentar errores en sus reglas de funcionamiento.

## 6. Qué se rechazó o qué se decidió no utilizar

Se decidió no concentrar toda la lógica del sistema dentro de los botones.

Tampoco se consideró apropiado utilizar expresiones lambda para todas las operaciones, ya que las funciones con nombre son más claras cuando se implementan reglas complejas.

Se mantuvo una separación entre la interfaz y las funciones que calculan los resultados del combate.

## 7. Criterio personal sobre el uso de IA

La inteligencia artificial fue utilizada como herramienta de apoyo y no como sustituto de la comprensión del código.

El funcionamiento de la aplicación debe comprobarse mediante pruebas, y cada concepto utilizado debe poder explicarse con ejemplos.

El uso de IA permite acelerar algunas tareas, pero las decisiones técnicas, la revisión de los resultados y la comprensión de la programación funcional siguen siendo responsabilidad del estudiante.