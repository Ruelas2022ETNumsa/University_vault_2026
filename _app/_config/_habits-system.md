---
title: Sistema de Habits — University Vault
galaxy_body: beacon
scope: vault
audience:
  - usuario
  - claude
related_notes:
  - "[[_galaxy-system]]"
  - "[[_projects_system]]"
tags:
  - beacon
  - habits
  - infraestructura
date_created: 2026-09-03
date_updated: 2026-09-03
status: activo
---

# Sistema de Habits — University Vault

> Sistema Galaxy: [[_galaxy-system]]
> Sistema de Proyectos: [[_projects_system]]

Plugin: **Habits** (jamescliffordspratt) — tracker de hábitos diarios con streaks, estadísticas y reportes. Cada hábito es un archivo `.md` con frontmatter propio. Sin base de datos externa — todo vive en el vault.

---

## Carpeta del sistema

```
Habits/
```

Carpeta raíz única — el plugin no soporta subcarpetas. Todos los archivos de hábito deben estar en este nivel. Los archivos de dashboard (sin `habit: true`) coexisten en la misma carpeta sin ser detectados como hábitos.

---

## Tipos de hábito

| `type`      | Rol                                                         | Interacción          |
| ----------- | ----------------------------------------------------------- | -------------------- |
| `binary`    | Sí/No por día — hecho o no hecho                           | Toggle               |
| `repetition`| Contador con unidad y target diario                        | Botones +1 / +N      |

> El tipo `duration` no existe en este plugin — usar `repetition` con `unit: minutos` o `unit: segundos` para trackear tiempo.

---

## Estructura de un archivo de hábito

Cada hábito es un `.md` con `habit: true` en el frontmatter. El plugin escribe los `records` automáticamente al loggear desde el dashboard o el sidebar.

```yaml
---
habit: true
type: binary                  # binary | repetition
target: N                     # requerido si type: repetition
unit: "unidad"                # requerido si type: repetition
color: "#HEXCODE"             # color individual de la card
group: NombreGrupo            # agrupa visualmente en el dashboard
tags:
  - etiqueta
icon: nombre-lucide           # ícono Lucide (dumbbell, cpu, footprints...)
useGroupColor: true           # hereda el color del grupo en lugar del color individual
startDate: YYYY-MM-DD
weeklyTarget: N               # días por semana esperados
records:
  YYYY-MM-DD: 1               # escritos automáticamente por el plugin
---
```

---

## Grupos activos

Los grupos separan visualmente los hábitos en el dashboard cuando la opción **Enable groups** está activada en Settings. En el sidebar lateral la separación no se refleja — todos aparecen juntos.

| Grupo      | Color base  | Descripción                              |
| ---------- | ----------- | ---------------------------------------- |
| `Ejercicio`| individual  | Rutina de fuerza con mancuernas          |
| `Cardio`   | individual  | Caminata diaria a la facultad            |
| `Workers`  | `#9B59B6`   | Control de uso diario de workers del hangar |

---

## Archivos del sistema

### Hábitos — Ejercicio

| Archivo                    | Type       | Target | Icono          | WeeklyTarget |
| -------------------------- | ---------- | ------ | -------------- | ------------ |
| `Curl Supino.md`           | binary     | —      | dumbbell       | 1            |
| `Curl de Martillo.md`      | binary     | —      | hammer         | 1            |
| `Extension de Triceps.md`  | binary     | —      | zap            | 1            |
| `Press de Banca.md`        | binary     | —      | activity       | 1            |
| `Press Militar.md`         | binary     | —      | arrow-up       | 1            |
| `Elevaciones Laterales.md` | binary     | —      | move-horizontal| 1            |
| `Dominadas.md`             | binary     | —      | chevrons-up    | 1            |
| `Abdominales.md`           | binary     | —      | flame          | 1            |

### Hábitos — Cardio

| Archivo                 | Type       | Target      | Icono      | WeeklyTarget |
| ----------------------- | ---------- | ----------- | ---------- | ------------ |
| `Caminata Facultad.md`  | repetition | 2 veces/día | footprints | 5            |

### Hábitos — Workers

Registran si un worker fue usado en el día. Nombres con prefijo numérico para ordenamiento consistente con la tabla del logbook.

| Archivo         | Worker    | WeeklyTarget |
| --------------- | --------- | ------------ |
| `1_alx_hot.md`  | alx_hot   | 7            |
| `2_krajo.md`    | krajo     | 7            |
| `3_alx_gml.md`  | alx_gml   | 7            |
| `4_alxrul.md`   | alxrul    | 7            |
| `5_alx-rul.md`  | alx-rul   | 7            |

> Los nombres de archivo de workers tienen prefijo `N_` para reflejar el orden de la tabla en `_hangar/bay/logbook.md` y para forzar el ordenamiento alfabético correcto en el explorador.

---

## Archivos de dashboard

No tienen `habit: true` — el plugin los ignora. Son notas de referencia que contienen bloques `habits` y `habit-metrics`.

| Archivo           | Contenido                                                        |
| ----------------- | ---------------------------------------------------------------- |
| `Dashboard.md`    | Carousel central con todos los hábitos (ejercicio + workers)     |
| `Rutina Fisica.md`| Referencia de ejercicios, tabla semanal y métricas por ejercicio |
| `Workers.md`      | Métricas individuales de los 5 workers                           |

---

## Bloques disponibles

| Bloque           | Uso                                                              |
| ---------------- | ---------------------------------------------------------------- |
| ` ```habits ` | Carousel de hábitos del día — engloba todos los grupos           |
| ` ```habit-metrics ` | Métricas de un hábito específico — streak, heatmap, gráficos |

Uso de `habit-metrics` con hábito específico:

````markdown
```habit-metrics
habit: Curl Supino
```
````

---

## Configuración relevante del plugin

| Setting             | Valor activo | Descripción                                              |
| ------------------- | ------------ | -------------------------------------------------------- |
| Habits folder       | `Habits`     | Carpeta raíz — no soporta subcarpetas                   |
| Enable groups       | activado     | Separa hábitos por `group` en el dashboard               |
| Group key           | `group`      | Clave del frontmatter que define el grupo                |
| Use group color key | `useGroupColor` | Clave para heredar color del grupo                    |
| Icon key            | `icon`       | Clave del frontmatter para el ícono Lucide               |
| Color key           | `color`      | Clave del frontmatter para el color individual           |

---

## Limitaciones conocidas

- **Sin subcarpetas** — todos los `.md` deben estar en `Habits/`. Mover un archivo a una subcarpeta lo saca del radar del plugin.
- **Sin timer interno** — el tipo `repetition` con unidad de tiempo es manual; el usuario carga el valor, el plugin no mide.
- **Groups en sidebar** — la separación por grupos solo funciona en el dashboard; el panel lateral muestra todos juntos sin distinción de grupo.
- **useGroupColor** — la herencia de color por grupo requiere activar la opción en Settings; sin activarla, el campo en el frontmatter no tiene efecto.

---

%%
# galaxy-links
[[_app/_config/_galaxy-system.md]]
[[_app/_config/_projects_system.md]]
[[_hangar/bay/logbook.md]]
%%
