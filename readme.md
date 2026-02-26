# Principios SOLID

Los principios SOLID son cinco recomendaciones de diseño de software que ayudan a escribir código más **legible, limpio, mantenible y escalable**. Su objetivo principal es facilitar los cambios futuros sin generar errores o afectar partes que ya funcionan.

> Los principios no solo aplican a programación orientada a objetos, sino también a frameworks modernos como React y Angular, e incluso al desarrollo backend.

---

## 1. S — Principio de Responsabilidad Única (SRP)

Una clase, función, módulo o componente debe tener **una sola razón para cambiar**.

**❌ Problema:** Un componente que hace peticiones a una API, filtra datos, maneja lógica de negocio *y* renderiza la vista está incumpliendo el principio.

**✅ Solución:** Separar responsabilidades:
- Un servicio para la API
- Otro servicio para el filtrado
- Un componente solo para mostrar datos

**🔍 Cómo detectarlo:**
- Una clase o componente hace demasiadas cosas
- Cambiar la lógica obliga a modificar la interfaz
- Los tests requieren muchos mocks para probar una sola unidad

---

## 2. O — Principio Abierto/Cerrado (OCP)

El software debe estar **abierto para extensión** y **cerrado para modificación**.

Se debe poder agregar nueva funcionalidad sin modificar código que ya funciona.

**❌ Problema:** Usar múltiples `if` o `switch` para manejar distintos casos. Cada nuevo tipo obliga a modificar la función original.

**✅ Solución:** Usar abstracciones, objetos de configuración o patrones que permitan agregar nuevos comportamientos sin tocar el código base.

**🔍 Cómo detectarlo:**
- Cada nuevo requerimiento implica modificar condicionales existentes
- El código crece con muchos `if` anidados

---

## 3. L — Principio de Sustitución de Liskov (LSP)

Las subclases o implementaciones deben poder **sustituir a su clase base** sin alterar el comportamiento esperado.

**❌ Problema:** Un servicio devuelve un `Observable`, pero su versión mock devuelve un array normal. Esto rompe el flujo esperado.

**✅ Solución:** Definir interfaces claras y asegurarse de que todas las implementaciones respeten el contrato.

**🔍 Cómo detectarlo:**
- Errores al reemplazar una implementación por otra
- Cambios de tipos inesperados
- Tests que fallan al usar mocks

---

## 4. I — Principio de Segregación de Interfaces (ISP)

No se debe obligar a una clase o componente a depender de métodos o propiedades que **no utiliza**.

Es preferible tener varias interfaces pequeñas y específicas que una grande y genérica.

**❌ Problema:** Interfaces muy grandes con métodos opcionales porque no todos los consumidores usan todo.

**✅ Solución:** Dividir en interfaces más pequeñas según responsabilidades.

**🔍 Cómo detectarlo:**
- Interfaces gigantes
- Props opcionales que casi nunca se usan
- Funciones que reciben objetos completos pero solo utilizan una parte

---

## 5. D — Principio de Inversión de Dependencias (DIP)

Las clases deben depender de **abstracciones**, no de implementaciones concretas.

**❌ Problema:** Instanciar directamente una clase dentro de otra (`new EmailClient()`).

**✅ Solución:** Depender de una interfaz (ej. `Notifier`) e inyectar cualquier implementación válida.

Esto facilita el **testing**, el uso de **mocks** y el **cambio de implementación** sin modificar la clase principal.

**🔍 Cómo detectarlo:**
- Uso frecuente de `new` dentro de clases
- Dependencias importadas e instanciadas directamente
- Dificultad para hacer pruebas unitarias

---

## Resumen rápido

| Letra | Principio | Idea clave |
|-------|-----------|------------|
| **S** | Single Responsibility | Una sola razón para cambiar |
| **O** | Open/Closed | Extender sin modificar |
| **L** | Liskov Substitution | Las implementaciones respetan el contrato |
| **I** | Interface Segregation | Interfaces pequeñas y específicas |
| **D** | Dependency Inversion | Depender de abstracciones, no de concretos |

---

## Ejemplos prácticos en JavaScript (sencillos)

Fueron creadas carpetas separadas para demostrar cada principio:

- `01-SRP/index.js`
- `02-OCP/example.js`
- `03-LSP/index.js`
- `04-ISP/index.js`
- `05-DIP/index.js`

### Cómo ejecutar

Desde la carpeta raíz del proyecto, ejecutar por ejemplo:

```bash
node 01-SRP/index.js
node 02-OCP/example.js
node 03-LSP/index.js
node 04-ISP/index.js
node 05-DIP/index.js
```

### Conclusion

- **SRP:** una clase, una responsabilidad.
- **OCP:** agregar sin modificar lo existente.
- **LSP:** una subclase no debe romper el comportamiento esperado.
- **ISP:** cada clase usa solo lo que necesita.
- **DIP:** depender de abstracciones e inyectar dependencias.