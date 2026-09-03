---
galaxy_body: blueprint
status: evaluando
priority: media
date: 2026-09-03
---

# Ideas Claude → TARS Integration

> **Relación:** Integración del flujo de trabajo Claude (IA) con la calculadora HP Prime G2 (TARS) y su emulador (CASE), donde Claude genera programas y datos que se transfieren y ejecutan en la calc.

---

## Flujo base verificado

- [x] Carpeta de trabajo compartida: `E:\University_vault_2026\_app\Tars\work`
- [x] Connectivity Kit detecta archivos en esa carpeta
- [x] Connectivity Kit puede transferir a TARS (USB) y CASE (red IP) simultáneamente
- [ ] Verificar flujo completo: Claude escribe archivo → Connectivity Kit lo detecta → se carga en CASE → se ejecuta

---

## Tipos de archivo generables por Claude

- [ ] `.hpprgm` — programa HP PPL puro → Claude escribe texto plano con sintaxis PPL, listo para cargar
- [ ] `.hpprgm` con Python embebido — wrapper PPL + bloque `#PYTHON ... #END` → útil para lógica más compleja
- [ ] `.hpnote` — nota de texto (UTF-16) → para documentación en la calc o datos en texto
- [ ] `.hpmat` / `.hplist` — matrices y listas en formato binario → factible pero requiere encoder; evaluar si vale la pena vs. generarlas desde PPL

---

## Casos de uso para electrónica (ingeniería)

- [ ] Conversor de unidades con prefijos SI (kilo, mega, mili, micro, nano, pico) — caso de uso inicial
- [ ] Calculadora de ley de Ohm + potencia (V, I, R, P) con entrada interactiva
- [ ] Divisor de tensión — calcular R1/R2 dado Vin y Vout objetivo
- [ ] Cálculo de impedancia compleja Z = R + jX (fasores)
- [ ] Análisis de circuitos RC/RL: frecuencia de corte, tiempo de carga
- [ ] Conversor de número binario/hex/decimal con display de 16 bits (alineado con config HEX 16 bits de TARS)
- [ ] Resolución de sistemas de ecuaciones para análisis nodal (MNA) — referencia: repo ECE_Analysis_Tools (UBC)

---

## MicroPython — posibilidades específicas

- [ ] Lógica de algoritmos más complejos que PPL (funciones recursivas, manejo de strings)
- [ ] Llamadas a CAS vía `hpprime.eval('...')` desde Python — permite combinar lógica Python con el CAS de la calc
- [ ] Input interactivo con `hpprime.keyboard()` y touch con `hpprime.eval('mouse')`
- [ ] Dibujo en pantalla para visualizaciones (gráficos simples, barras, indicadores)
- [ ] Limitación clave: no numpy — matrices vía `linalg.matrix` del módulo `hpprime`

---

## Repositorios de referencia

- [ ] Revisar `Dipto9999/ECE_Analysis_Tools` — programas PPL para MNA, fasores, root locus (electrónica UBC)
- [ ] Revisar `eried/PrimeComm` — herramienta para envío/conversión de archivos desde PC a la calc por CLI
- [ ] Revisar `BeatSkip/PrimeDev` — IDE web para G2, edición y transferencia de PPL y Python

---

## Estructura de carpeta de trabajo

- [ ] Definir convención de nombres para archivos generados por Claude en `_app/Tars/work/`
- [ ] Evaluar si conviene subcarpetas por tipo (ppl/, python/, data/) o todo plano
- [ ] Documentar en `HP_Prime_guide.md` el flujo final una vez probado

---

## Ideas migradas desde blueprint TI-Nspire

> Originalmente pensadas para TI-Nspire CX II CAS — adaptadas a HP Prime G2. El flujo es más simple porque `.hpprgm` es texto plano, sin cifrado ni conversión intermedia.

- [ ] **Flujo bidireccional vault ↔ calc** — en TI era `.md ↔ .tns` vía TnsTools + Luna (complejo). En HP Prime: Claude escribe `.hpprgm` directamente en `_app/Tars/work/` sin conversión. El flujo inverso (leer un programa desde la calc al vault) requiere exportar desde el Connectivity Kit.
- [ ] **Botones en Obsidian con Shell Commands + Commander** — disparar la apertura de la carpeta `work/` o el Connectivity Kit directamente desde la paleta de Obsidian. Aplica igual que en el blueprint TI.
- [ ] **Colección de programas de ingeniería de referencia** — equivalente al repo `sononicola/Ti-Nspire-CX-CAS-programs`. Para HP Prime: `Dipto9999/ECE_Analysis_Tools` (MNA, fasores, root locus). Revisar estructura para tomar convenciones.
- [ ] **Carpeta staging en el vault** — `_app/Tars/work/` ya cumple el rol de carpeta intermedia que se planificaba como `_calculadora/` en el flujo TI. Está resuelto.
- [ ] **Hojas de cálculo** — en TI existía como tipo nativo `.tns Spreadsheet`. En HP Prime no hay equivalente de archivo; se resuelve con la Spreadsheet App cargada con datos vía programa PPL, o matrices definidas en código.

---

## A depurar

- `.hpmat` y `.hplist` son formato binario con estructura documentada (TI-Planet wiki) — evaluar si construir un encoder Python simple o simplemente inicializar matrices desde PPL en la calc directamente
- Python en HP Prime es "beta" según firmware 2.4 — testear estabilidad antes de depender de él para casos de uso críticos
- El Connectivity Kit no siempre detecta archivos nuevos automáticamente — puede necesitar refresh manual o drag & drop
- Shell Commands + Commander (plugins Obsidian) — evaluar si ya están instalados en el vault antes de planificar integración
