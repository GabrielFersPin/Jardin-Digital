# SQL

- Operaciones sobre tablas
- Creación de una tabla
    
    CREATE TABLE PLANTA
    (id_planta integer primary key not null
    ciudad
    varchar (50)
    provincia
    varchar (50)
    direccion
    varchar (100)
    );
    
- Actualizar Registros existentes
    
    UPDATE TABLE <table name> SET campo =valor WHERE condition;
    
- Borrar una tabla
    
    DROP TABLE <table name>;
    
- Vaciar una tabla
    
    TRUNCABLE TABLE <table_name>;
    
- Clausula SELECT

SELECT (DISTINCT) * FROM <table_name > WHERE condition > GROUP BY <campo> HAVING <condition > ORDER BY <campo> desc

- SELECT
- FROM
- WHERE
    
    Condición para seleccionar un subconjunto de registros
    
- GRUOP BY
    
    Campos sobre los que realiza la agrupación
    
- HAVING
    
    Condición sobre la agragación
    
- ORDER BY
    
    Campo o campos para especificar el orden de la salida de registros
    
- Funciones de Agregación
- min, max, count, sum
- std, avg
- JOIN
- Sintaxis general
    
    SELECT <campos>from
    
    <tableA>A
    
    JOIN
    
    <tableB>B
    
    on [A.id](http://A.id) = B.id
    
- Diagrama de funcionamiento de SQL
    
    ![Untitled](Export-d7e8ae6d-ef3b-4f55-8be3-1b817dca48a9/Data%20Science%20Studies%20a8e59d9bdca84dd9b0e12dbb12171baf/Estructura%20y%20Análisis%20de%20Datos%2098add004394d41fbb6fdb943fa596a01/SQL/Untitled.png)