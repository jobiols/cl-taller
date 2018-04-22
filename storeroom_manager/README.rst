===============
Manejo de pañol
===============

Cuando un mecánico requiera materiales, el pañolero creará en el sistema una
nueva orden de entrega de materiales. En el encabezado de la orden podrá
ingresar el número de la orden de trabajo y algunos otros datos según se
requiera tales como fecha, nombre del mecánico, dominio del vehículo, etc.
Continuará seleccionando productos y cantidades para llenar la orden de
entrega. La selección de los productos se realizará con un filtro de múltiples
criterios como ser parte del nombre del producto, la marca del vehículo,
modelo y serie al que pertenece el producto, el proveedor del producto, etc.
Una vez seleccionado el producto se mostrará código descripción y lugar de
ubicación dentro del pañol y se permitirá ingresar la cantidad de producto a
entregar.

Al seleccionar los productos el sistema alertará si se intenta agregar a la
orden un producto del cual no hay stock, sin embargo el pañolero podrá
ignorar esta advertencia y generar la orden de todos modos.
En este caso al validar la orden el valor de stock del producto en cuestión
pasará a negativo
La orden de entrega se generará en estado borrador y podrá imprimirse y/o
modificarse. Al Validar la orden pasará al estado Validado y bajará de stock
los productos que contengan.


