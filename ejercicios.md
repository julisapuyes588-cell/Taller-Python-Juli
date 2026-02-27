# Taller de Python - Manejo de Datos

## Dataset
Archivo: `data/personas.csv` con 300,000 registros.

Los campos `nombre_cifrado` y `apellido_cifrado` usan cifrado ROT13. El resto de columnas tienen datos sucios (espacios, caracteres especiales como @, %, #, etc.).

Para descifrar ROT13: `codecs.decode(texto, 'rot_13')`

---

## Ejercicios

1. ¿Cuántas filas tienen el campo `id` con caracteres no numéricos?

2. ¿Cuántas veces aparece el nombre "Maria" en el dataset?

3. ¿Cuántas veces aparece el nombre "Juan" en el dataset?

4. ¿Cuál es el nombre más frecuente en el dataset y cuántas veces aparece?

5. ¿Cuál es el apellido más frecuente en el dataset y cuántas veces aparece?

6. ¿Cuántos registros tienen la ciudad "Bogota" después de limpiar espacios y caracteres especiales?

7. ¿Cuántos registros tienen la ciudad "Medellin" después de limpiar los datos?

8. ¿Cuántas ciudades únicas existen en el dataset después de normalizar los datos?

9. ¿Cuántos registros tienen la profesión "Ingeniero" después de limpiar los datos?

10. ¿Cuántos registros tienen la profesión "Programador" después de limpiar los datos?

11. ¿Cuántas profesiones únicas existen en el dataset después de normalizar los datos?

12. ¿Cuántos registros tienen el campo `email` con espacios adicionales?

13. ¿Cuántos registros tienen el campo `salario` con caracteres no numéricos?

14. ¿Cuál es el salario promedio después de limpiar y convertir la columna a numérico?

15. ¿Cuál es el salario máximo después de limpiar los datos?

16. ¿Cuál es el salario mínimo después de limpiar los datos?

17. ¿Cuántos registros tienen el campo `activo` como verdadero después de normalizar los valores (True, true, 1, Si, yes, etc.)?

18. ¿Cuántos registros tienen el campo `activo` como falso después de normalizar los valores?

19. ¿Cuántos registros tienen la fecha de nacimiento con formato diferente a YYYY-MM-DD?

20. ¿Cuántas personas nacieron entre 1990 y 2000 (inclusive) después de limpiar las fechas?

21. ¿Cuántas personas nacieron antes de 1960 después de limpiar las fechas?

22. ¿Cuántas personas tienen más de 50 años (considerando fecha actual 2026-02-26)?

23. ¿Cuántos registros tienen el nombre "Carlos" y viven en "Cali"?

24. ¿Cuántos registros tienen el nombre "Ana" y son "Medico"?

25. ¿Cuántos registros tienen profesión "Abogado" y salario mayor a 10,000,000?

26. ¿Cuántos registros tienen ciudad "Barranquilla", están activos y nacieron después de 1980?

27. ¿Cuál es la ciudad con más "Ingenieros"?

28. ¿Cuál es la profesión con el salario promedio más alto?

29. ¿Cuántos registros tienen el email con dominio "gmail.com" después de limpiar los datos?

30. ¿Cuántos registros tienen exactamente la combinación nombre "Jose" y apellido "Garcia"?
