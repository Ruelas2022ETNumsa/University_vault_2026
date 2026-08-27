---
skill: "Claude Start Móvil"
scope: "session-init-mobile"
activates: "Al recibir /drive en instrucciones de Claude"
requires: "Google Drive MCP — solo lectura"
status: active
---

# _start_movil

Leé este archivo y seguí el flujo exactamente.
Este modo es de **solo consulta** — sin editar, mover ni crear archivos en el vault.
Usás el **MCP de Google Drive** (conector nativo de claude.ai) para todo acceso al vault.

---

## Selección de modo

Respondé exactamente esto y esperá:

```
Modos disponibles:

1. repaso  — consulta de notas, ejercicios y teoría
2. plan    — planificación de estudio y organización

Comandos:
/tokens  — hora en que se reestablecen los tokens
/close   — cierra la sesión
```

---

## Carga del modo

Según la opción elegida, buscá el archivo en Drive y ejecutá su flujo:

| Opción | Archivo a buscar en Drive    |
| ------ | ---------------------------- |
| repaso | [[_skills/_repaso_movil.md]] |
| plan   | [[_plan_movil]]   |

---

## Acceso al vault via Drive

El vault está sincronizado en Google Drive. Las dos carpetas principales para este modo:

- **`MOC/`** — índices por materia (stars). Empezá acá para orientarte en un tema.
- **`Semesters/`** — todas las notas académicas organizadas por semestre y materia.

Para leer un archivo: buscalo por título usando el MCP de Drive.
Si el archivo no aparece, intentá con parte del nombre.

---

## Navegación con galaxy-links

Cada nota tiene un bloque `%%galaxy-links%%` al final con wikilinks al estilo:
`[[Semesters/Sem_01/MAT101/Partial_1/T00/nombre-nota.md]]`

Para navegar: leé el bloque `%%` de la nota actual → tomá el título del wikilink → buscalo en Drive por nombre.

---

## Imágenes

Si una nota referencia una imagen disponible en Drive:
1. Buscá el archivo por nombre en Drive
2. Obtené su `viewUrl`
3. Mostrá el link: `[Ver imagen](viewUrl)`

El usuario la abre en una pestaña sin descargar nada.

> **Nota:** `_assets/` no está sincronizada con Drive aún. Los SVGs de plugins sí están disponibles.

---

## Control de tokens

La hora de inicio se indica en el mensaje de apertura como:
`Hora de inicio: HH:MM`

Cuando el usuario escriba **`/tokens`** → respondé exactamente:
`Tokens se reestablecen a las HH:MM` (hora_inicio + 5 horas)

---

## Cierre de sesión

Cuando el usuario escriba **`/close`** → respondé:
`Sesión móvil cerrada.`

---

## Prohibiciones

- Sin edición de archivos en Drive
- Sin mover ni renombrar archivos
- Sin crear notas `.md` directamente en Drive durante la sesión
- Sin acceso a GitHub MCP
