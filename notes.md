__pycache__/

Es una carpeta que Python crea sola cuando ejecutas o importas código. Dentro guarda versiones precompiladas de tus archivos (.pyc) para que la próxima vez arranquen más rápido.

Son archivos automáticos que se regeneran cuando hace falta, no contienen nada tuyo y no aportan nada en GitHub, solo ruido. Por eso se ignoran.

Puede que no la veas todavía en tu proyecto. Aparece cuando importas tus propios módulos, y si no existe, esa línea simplemente no hace nada.
Notas: PCA + regresión logística (dataset del corazón)

# Notas: PCA + regresión logística (dataset del corazón)

Fecha: 2026-10-26

## 1. ¿Qué estamos intentando hacer? (la idea en una frase)

Tenemos datos de pacientes (edad, colesterol, presión...) y queremos que un
modelo **adivine si el paciente tiene enfermedad del corazón o no**.

- Lo que queremos adivinar → columna `target` (0 = no, 1 = sí). Es **y**.
- Los datos para adivinarlo → las otras 13 columnas. Es **X**.

Como la respuesta es una de dos opciones (0 o 1), esto es un problema de
**clasificación**. Por eso se usa `LogisticRegression` (a pesar del nombre,
sirve para clasificar, no para predecir números).

## 2. El código, paso a paso

```
 heart.csv
    │
    ▼
 1. Cargar los datos            pd.read_csv()
    │
    ▼
 2. Separar X (13 cols) e y     drop(['target'])
    │
    ▼
 3. Poner todo en la misma      StandardScaler()
    escala
    │
    ▼
 4. Dividir en entrenamiento    train_test_split()
    (70%) y prueba (30%)
    │
    ▼
 5. Reducir 13 columnas a 3     PCA(n_components=3)
    │
    ▼
 6. Entrenar el modelo          logistic.fit(...)
    │
    ▼
 7. Evaluar con los datos       logistic.score(...)
    de prueba
```

### Paso 3: StandardScaler
Las columnas están en escalas muy distintas (edad ~50, colesterol ~250,
`oldpeak` ~1.5). Sin escalar, las columnas con números grandes pesarían más
solo por su tamaño. El scaler las deja todas con media 0 y dispersión parecida.

### Paso 4: train_test_split
Separamos los datos en dos grupos:
- **Entrenamiento (70%)**: el modelo aprende con estos.
- **Prueba (30%)**: datos que el modelo **nunca ha visto**, para comprobar
  si aprendió de verdad o solo memorizó.

Es como estudiar con unos ejercicios y examinarte con otros distintos.

`random_state=42` hace que el reparto sea siempre el mismo y los resultados
se puedan repetir.

### Qué significa (717, 13)
Es el tamaño de los datos de entrenamiento: **717 filas** (pacientes) y
**13 columnas** (variables, sin contar `target`).
- `print(dt_heart.head(5))` dice `[5 rows x 14 columns]`: son 5 filas de
  muestra y 14 columnas (las 13 más `target`).
- `(717,)` es `y_train`: una sola columna, la respuesta de cada paciente.

### Paso 5: PCA
Tenemos 13 variables, y muchas se parecen entre sí o aportan poco. PCA no
elimina variables: **las mezcla** y crea 3 nuevas (combinaciones de las 13)
diseñadas para guardar la mayor cantidad de información posible.

- Ventaja: datos más simples y rápidos de procesar.
- Coste: se pierde algo de información.

La gráfica de `explained_variance_ratio_` muestra cuánta información guarda
cada componente nueva.

### PCA vs IncrementalPCA
Hacen lo mismo, pero IncrementalPCA procesa los datos en grupos pequeños
(`batch_size=10`). Sirve cuando los datos son tan grandes que no caben en la
memoria. Aquí el dataset es pequeño, así que es solo para comparar.

### fit y transform
- `fit(...)`: el modelo **aprende** de los datos.
- `transform(...)`: **aplica** lo aprendido para cambiar los datos
  (aquí, pasar de 13 columnas a 3).

## 3. ¿Qué es el score?

Es el **porcentaje de aciertos** del modelo sobre los datos de prueba
(en este caso se llama *accuracy*).

```
score = predicciones correctas / total de pacientes de prueba
```

Nuestros resultados:

| Método | Score  | Qué significa                              |
|--------|--------|--------------------------------------------|
| PCA    | 0.7857 | acierta ~78.6% de los pacientes de prueba  |
| IPCA   | 0.8052 | acierta ~80.5% de los pacientes de prueba  |

Los datos de prueba son 308 pacientes (30% de 1025). Entonces:
- PCA acertó con 242 de 308.
- IPCA acertó con 248 de 308.

### ¿IPCA es mejor entonces?
No se puede asegurar. La diferencia es de **6 pacientes** y se ha medido con
un solo reparto de datos. Con otro `random_state` podría salir al revés.
Lo honesto es decir: "los dos rinden parecido".

## 4. Cosas para probar (así se entiende de verdad)

1. Cambia `n_components=3` por 2, 5 y 13. ¿Cómo cambia el score?
2. Entrena la regresión logística **sin PCA** (con las 13 columnas) y compara.
   Así sabes cuánto te cuesta (o ayuda) reducir la dimensión.
3. Imprime `sum(pca.explained_variance_ratio_)` para ver qué porcentaje de la
   información total conservan los 3 componentes.
4. Cambia `random_state=42` por otro número y mira si el score cambia mucho.

## 5. Para más adelante (no urgente)

El `StandardScaler` se ajusta con **todos** los datos antes de dividir en
entrenamiento y prueba. Lo ideal es ajustarlo solo con los de entrenamiento y
luego aplicarlo a los de prueba, para que la prueba sea 100% "no vista".
El efecto aquí es pequeño, pero es un buen hábito.

## 6. Lo que no entiendo todavía

- [ ] (escribe aquí tus dudas)
- [ ]

## 7. Siguiente paso

- [ ] Hacer los experimentos de la sección 4 y apuntar los resultados.