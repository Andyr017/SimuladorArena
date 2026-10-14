# Análisis funcional del proyecto Arena Funcional

## 1. Problema que resuelve la aplicación

Arena Funcional es una aplicación desarrollada en Python que simula un sistema de combate entre un jugador y diferentes enemigos. Permite realizar ataques, recuperar puntos de vida, ejecutar ataques especiales y consultar estadísticas del combate.

El objetivo del proyecto es aplicar los conceptos de programación funcional estudiados en las unidades 1 y 2 mediante una aplicación con interfaz gráfica.

La aplicación utiliza Tkinter y Ttk-Bootstrap para presentar la información de manera organizada y facilitar la interacción con el usuario.

## 2. Estructuras de datos utilizadas

El proyecto utiliza las siguientes estructuras:

- **Personaje:** representa al jugador mediante su nombre, vida actual, vida máxima, ataque y experiencia.
- **Enemigo:** representa a los enemigos mediante su nombre, vida actual, vida máxima, ataque y recompensa.
- **Tuplas:** se utilizan para almacenar la colección inicial de enemigos y representar colecciones que no necesitan modificarse directamente.
- **Listas:** se utilizan para registrar el historial de eventos del combate.
- **Funciones:** organizan las reglas del juego y permiten separar la lógica de la interfaz.

Las estructuras Personaje y Enemigo se definen mediante `dataclass` con `frozen=True`, lo que impide modificar directamente los atributos de sus instancias.

## 3. Aplicación de la Unidad 1

### 3.1. Funciones de orden superior

Se utilizan funciones de orden superior y herramientas funcionales para procesar información.

En `logica.py`, la función `filtrar_enemigos_derrotados()` utiliza `filter()` para seleccionar los enemigos cuya vida ha llegado a cero.

La función `obtener_nombres_enemigos()` utiliza `map()` para obtener los nombres de los enemigos.

La función `calcular_experiencia_total()` utiliza `reduce()` para sumar las recompensas de una colección de enemigos.

También se implementa `crear_multiplicador()`, que devuelve otra función. Esto permite configurar una operación y utilizarla posteriormente.

### 3.2. Pattern matching con match/case

La función `procesar_accion()` utiliza `match/case` para decidir qué operación debe ejecutarse según la acción recibida.

Se contemplan los siguientes casos:

- `atacar`: calcula el daño y actualiza el estado del enemigo.
- `curar`: calcula la nueva vida del jugador.
- `case _`: gestiona las acciones no reconocidas.

Este recurso permite organizar las decisiones del sistema de manera clara y facilita la incorporación de nuevas acciones.

### 3.3. Modelado de datos

Se utilizan las clases `Personaje` y `Enemigo`, definidas mediante `dataclass`.

Esta decisión permite representar las entidades del juego mediante estructuras con atributos definidos y anotaciones de tipos.

El uso de `frozen=True` contribuye a mantener la inmutabilidad de las instancias.

### 3.4. Enfoque funcional frente al imperativo

En `logica.py` se incluyen las funciones `procesar_accion()` y `procesar_accion_imperativa()`.

La primera utiliza `match/case` y devuelve los resultados de la acción mediante nuevos objetos. La segunda utiliza instrucciones condicionales tradicionales para mostrar una alternativa de estilo imperativo.

La versión imperativa es una comparación didáctica y no reproduce todas las reglas de la versión principal. Por ello, la comparación se centra en la organización de las instrucciones y no en afirmar que ambas funciones son completamente equivalentes.

## 4. Aplicación de la Unidad 2

### 4.1. Uso de lambda

Las expresiones `lambda` se utilizan en distintas operaciones del programa.

Por ejemplo, en `filtrar_enemigos_derrotados()` se emplea una función lambda para comprobar si la vida de un enemigo es igual a cero.

También se utiliza `lambda` en `obtener_nombres_enemigos()` para obtener el nombre de cada enemigo, y en `calcular_experiencia_total()` para acumular las recompensas.

En la interfaz gráfica se utiliza `lambda` para asociar los botones de ataque y curación con las acciones correspondientes.

No conviene utilizar lambda para implementar reglas complejas, porque las funciones con nombre facilitan la lectura, las pruebas y el mantenimiento del código.

### 4.2. Closure

El closure se encuentra en la función `crear_multiplicador()`.

Esta función recibe un factor y devuelve otra función que utiliza ese valor para multiplicar un número.

En `calcular_ataque_especial()` se crea un multiplicador con un factor de 1.5. De esta manera, el ataque especial calcula un daño equivalente a una vez y media el ataque normal.

El closure permite configurar el comportamiento de una función sin tener que repetir la misma operación.

### 4.3. Inmutabilidad

La inmutabilidad se aplica mediante las estructuras `Personaje` y `Enemigo`, que utilizan `frozen=True`.

Para actualizar sus atributos se utiliza `dataclasses.replace()`, que crea una nueva instancia con los valores modificados.

Por ejemplo, cuando el personaje recibe daño, la función `recibir_danio()` devuelve un nuevo objeto con la vida actualizada, en lugar de modificar directamente el objeto original.

Esto permite comprender mejor cómo cambia el estado del sistema y reduce las modificaciones directas de los datos.

### 4.4. Funciones puras

Entre las funciones puras del proyecto se encuentran:

- `calcular_danio()`: calcula el daño a partir del ataque y la defensa.
- `recibir_danio()`: devuelve un nuevo personaje con la vida actualizada.
- `curar_personaje()`: calcula la vida recuperada y devuelve un nuevo personaje.
- `calcular_experiencia_total()`: suma las recompensas recibidas como entrada.
- `buscar_enemigo()`: busca un enemigo por su nombre dentro de una colección.

Estas funciones no modifican directamente los objetos recibidos ni actualizan la interfaz gráfica.

Sus resultados dependen de los argumentos proporcionados, lo que facilita su comprensión y comprobación.

### 4.5. Funciones impuras y efectos secundarios

Los efectos secundarios aparecen principalmente en la interfaz gráfica.

Por ejemplo, `registrar_evento()` agrega información al historial y modifica el contenido de un widget de texto.

La función `actualizar_interfaz()` modifica los valores y textos que aparecen en la ventana.

La función `limpiar_historial()` elimina el contenido visible del historial y modifica la lista de eventos.

Estas operaciones necesitan interactuar con el estado de la aplicación o con los componentes gráficos. Por ello, no deben considerarse funciones puras.

Separar estas operaciones de los cálculos de la lógica permite distinguir entre la toma de decisiones y la presentación de resultados.

## 5. Transformación inmutable del estado

Cuando el jugador ataca, recibe daño o se cura, el programa puede crear nuevas instancias de los objetos mediante `replace()`.

La interfaz recibe los resultados de las funciones de la lógica y actualiza las referencias al jugador o al enemigo correspondiente.

De esta manera, los atributos de las instancias originales no se modifican directamente.

Sin embargo, la aplicación sí mantiene un estado mutable en la capa visual, como la lista del historial y las referencias a los objetos actuales. Por tanto, la inmutabilidad se aplica a los modelos de datos, no a absolutamente todo el programa.

## 6. Closure implementado

El closure se encuentra en `crear_multiplicador()`.

La función externa recibe un factor y devuelve la función interna `multiplicar()`, que conserva el acceso a dicho factor.

En el proyecto se utiliza para configurar el multiplicador del ataque especial.

Esta implementación demuestra cómo una función puede conservar información de su entorno y utilizarla después de que la función externa haya terminado.

## 7. Uso de inteligencia artificial

Se utilizó inteligencia artificial como herramienta de apoyo durante el desarrollo.

La IA ayudó a proponer la estructura inicial del proyecto, organizar los archivos, implementar las funciones de la lógica y desarrollar una interfaz gráfica con Tkinter y Ttk-Bootstrap.

También proporcionó ejemplos para aplicar `dataclass`, `match/case`, funciones lambda, closures, inmutabilidad y herramientas como `map()`, `filter()` y `reduce()`.

La aplicación y sus explicaciones deben revisarse para garantizar que cada concepto esté correctamente implementado y que el estudiante comprenda su funcionamiento.

## 8. Correcciones y decisiones técnicas

Durante el desarrollo se ejecutó la aplicación y se comprobó el funcionamiento de sus principales controles.

Una decisión importante fue separar la lógica del combate de la interfaz gráfica. De esta forma, los botones no contienen todos los cálculos y las reglas del sistema.

También se utilizó `dataclass` con `frozen=True` y `replace()` para trabajar con nuevos estados de los personajes.

La función `procesar_accion_imperativa()` se incorporó como una comparación didáctica. No se considera una implementación idéntica a la versión principal, ya que no incluye todas sus reglas.

Como parte de la revisión final, se deben verificar especialmente las recompensas de experiencia, el registro de enemigos derrotados y el comportamiento del ataque especial.

## 9. Aprendizajes técnicos

El desarrollo del proyecto permitió practicar la separación entre interfaz, lógica y datos.

También permitió comprender la diferencia entre modificar directamente un objeto y crear una nueva instancia con valores actualizados.

Se practicó el uso de funciones de orden superior, expresiones lambda, closures y pattern matching.

Finalmente, se identificó que una interfaz gráfica requiere efectos secundarios, pero estos pueden mantenerse separados de las funciones que realizan los cálculos principales.

El proyecto demuestra que la programación funcional puede utilizarse para organizar reglas y transformaciones de datos dentro de una aplicación interactiva desarrollada en Python.