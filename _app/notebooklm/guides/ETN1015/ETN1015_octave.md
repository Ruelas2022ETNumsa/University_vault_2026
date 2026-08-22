---
title: Octave — Guía de adaptación desde MATLAB (ETN1015)
galaxy_body: beacon
scope: vault
tool: notebooklm
audience:
  - notebooklm
tags:
  - beacon
  - octave
  - matlab
  - infraestructura
  - ETN1015
date_created: 2026-08-20
date_updated: 2026-08-20
status: activo
---

# Guía de adaptación MATLAB → Octave — ETN1015

Esta guía documenta **únicamente las diferencias** entre MATLAB y Octave relevantes para ETN1015.
El flujo de resolución sigue siendo MATLAB (ver ETN1015_matlab.md).
Octave es el entorno de ejecución cuando MATLAB no está disponible.

Todo lo que no aparece aquí funciona igual en ambos entornos.

---

## 1. Regla fundamental

> **Si el código MATLAB usa solo operaciones básicas** (vectores, `fft`, `filter`, `conv`, `stem`, `plot`) corre en Octave sin cambios.
> **Si usa funciones de diseño de filtros** (`butter`, `fir1`, `freqz`, `zplane`, etc.) requiere `pkg load signal` al inicio.

---

## 2. Carga del paquete signal

En Octave, las funciones de diseño y análisis de filtros no están disponibles por defecto.
Requieren el paquete `signal`, que se carga así:

```octave
pkg load signal
```

Donde va: primera línea del script, antes de `clear; clc; close all;`

```octave
pkg load signal          % agregar solo en Octave
clear; clc; close all;
```

Funciones que requieren pkg load signal:

| Categoría | Funciones |
|---|---|
| Diseño IIR | `butter`, `buttord`, `cheby1`, `cheby2`, `ellip`, `cheb1ord`, `cheb2ord`, `ellipord` |
| Diseño FIR | `fir1`, `fir2`, `remez`, `kaiserord` |
| Análisis | `freqz`, `freqs`, `zplane`, `grpdelay`, `impz` |
| Multi-rate | `resample`, `decimate`, `upfirdn` |
| Transformación | `bilinear` |
| Ventanas | `chebwin`, `gausswin`, `flattopwin` |

Funciones que NO requieren pkg load signal (ya están en Octave base):

`fft`, `ifft`, `fftshift`, `filter`, `conv`, `stem`, `plot`, `subplot`,
`upsample`, `downsample`, `abs`, `angle`, `real`, `imag`, `zeros`, `ones`,
`blackman`, `hamming`, `hann`, `bartlett`, `rectwin`

---

## 3. Diferencia clave: freqz con y sin salida

### En MATLAB
`freqz(b, a)` sin salida genera la grafica automaticamente en una figura nueva.

### En Octave
`freqz(b, a)` sin salida puede comportarse diferente segun la version.
La forma segura y portable es siempre capturar la salida:

```octave
% MATLAB: funciona con o sin salida
freqz(b, a);                          % genera grafica automatica

% Octave: forma segura — capturar salida y graficar manualmente
[H, w] = freqz(b, a, 512);
figure;
subplot(2,1,1);
plot(w/pi, 20*log10(abs(H)));
xlabel('\omega / \pi'); ylabel('|H| [dB]'); title('Magnitud'); grid on;
subplot(2,1,2);
plot(w/pi, angle(H));
xlabel('\omega / \pi'); ylabel('Fase [rad]'); title('Fase'); grid on;
```

Regla: en codigo destinado a Octave, nunca usar `freqz(b, a)` sin capturar salida.
Siempre usar `[H, w] = freqz(b, a, N)` y graficar manualmente.

---

## 4. Diferencia: zplane

### En MATLAB
`zplane(b, a)` funciona directamente (requiere Signal Processing Toolbox).

### En Octave
`zplane(b, a)` funciona igual despues de `pkg load signal`. Sin cambios en el codigo.

```octave
pkg load signal
zplane(b, a);             % igual que en MATLAB
```

---

## 5. Diferencia: fir1 con orden impar para highpass/bandstop

### En MATLAB
Si se pasa orden impar para highpass o bandstop, MATLAB lo incrementa internamente sin aviso.

### En Octave
Octave emite un warning explicito:

```
warning: n must be even for highpass and bandstop filters. Incrementing.
```

El resultado es el mismo — el warning es informativo, no un error.
Para evitarlo, usar orden par desde el inicio:

```octave
% Genera warning en Octave si el orden es impar:
h = fir1(15, 0.4, 'high');

% Sin warning — usar orden par:
h = fir1(16, 0.4, 'high');
```

---

## 6. Funciones no disponibles en Octave

Estas funciones de MATLAB no existen en Octave ni en el paquete signal:

| Funcion MATLAB | Alternativa en Octave |
|---|---|
| `designfilt` | Usar `butter`, `cheby1`, `fir1`, etc. directamente |
| `filterDesigner` (GUI) | No disponible — disenar por codigo |
| `fdatool` (GUI) | No disponible — disenar por codigo |
| `fvtool` | Usar `freqz` + `zplane` manualmente |
| `upfirdn` | Disponible en signal — requiere `pkg load signal` |

Consecuencia practica: todo el codigo generado por ETN1015_matlab.md evita `designfilt` y GUIs
y usa funciones clasicas que si estan disponibles en Octave con `pkg load signal`.

---

## 7. Encabezado estandar para scripts Octave

```octave
pkg load signal              % cargar si el script usa filtros/freqz/zplane
% ETN1015 — [Tema / Capitulo Palani]
% Ejercicio: [enunciado breve]
% Entorno: Octave
clear; clc; close all;
```

Si el script no usa ninguna funcion del paquete signal, omitir la primera linea.

---

## 8. Tabla de compatibilidad por capitulo Palani

| Capitulo | Funciones usadas | Requiere pkg load signal |
|---|---|---|
| Cap. 1 — Discrete Signals | `fft`, `filter`, `conv`, `stem` | No |
| Cap. 2 — DFT y FFT | `fft`, `ifft`, `fftshift`, `abs`, `angle` | No |
| Cap. 3 — Filtros IIR | `butter`, `cheby1`, `ellip`, `freqz`, `zplane`, `bilinear` | Si |
| Cap. 4 — Filtros FIR | `fir1`, `fir2`, `freqz` | Si |
| Cap. 5 — Word Length | `round`, `floor`, `filter` | No |
| Cap. 6 — Multi-rate | `upsample`, `downsample`, `resample`, `decimate` | Parcial* |

*`upsample` y `downsample` son de Octave base. `resample` y `decimate` requieren `pkg load signal`.

---

## 9. Diferencias menores de sintaxis

Estas diferencias existen entre Octave y MATLAB pero no afectan los scripts de ETN1015
porque el codigo generado evita estas construcciones:

| Construccion | MATLAB | Octave | Afecta ETN1015 |
|---|---|---|---|
| Indexacion encadenada | `size(x)(2)` falla | `size(x)(2)` funciona | No |
| Comentarios | Solo `%` | `%` y `#` | No — usamos solo `%` |
| Operadores de incremento | No soporta `++` | Soporta `++` | No |
| `atan2(-0, -0)` | Retorna `0` | Retorna `-pi` | No afecta DSP estandar |
| Strings dobles `"..."` | Char array | Igual que `'...'` | No — usamos `'...'` siempre |

---

## 10. Flujo de adaptacion MATLAB a Octave

Dado un script MATLAB generado con ETN1015_matlab.md:

1. Usa `designfilt`, `fdatool` o `filterDesigner`?
   Reemplazar por la funcion clasica equivalente (`butter`, `fir1`, etc.)
   No deberian aparecer si el codigo sigue ETN1015_matlab.md

2. Usa `freqz`, `butter`, `fir1`, `zplane` u otra funcion de la tabla seccion 2?
   Agregar `pkg load signal` como primera linea

3. Usa `freqz(b, a)` sin capturar salida?
   Reemplazar por `[H, w] = freqz(b, a, 512)` + grafica manual (ver seccion 3)

4. Usa `fir1` con orden impar para highpass/bandstop?
   Cambiar a orden par para evitar warning (ver seccion 5)

5. El resto del codigo corre sin cambios.

---

%%
# galaxy-links
[[ETN1015_matlab.md]]
[[ETN1015_latex.md]]
%%