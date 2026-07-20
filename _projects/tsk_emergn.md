---
status: creciente
---




---

## Supercharged Links — Sistema de status lunar para archivos `tsk`

### Plugin
**Obsidian Supercharged Links**
Repositorio: https://github.com/mdelobelle/obsidian_supercharged_links

Muestra iconos/prefijos en la barra lateral izquierda del vault según el valor de un campo YAML. Ya instalado y funcionando.

---

### CSS snippet
**Archivo:** `E:\University_vault_2026\.obsidian\snippets\supercharged-status.css`

Mapea el campo `status` del frontmatter a un emoji lunar visible en el explorador de archivos de Obsidian:

```css
.nav-file-title-content[data-link-status="nueva"]::before {
    content: "🌑 ";
}
.nav-file-title-content[data-link-status="creciente"]::before {
    content: "🌒 ";
}
.nav-file-title-content[data-link-status="llena"]::before {
    content: "🌕 ";
}
```

---

### Sistema de status
Solo aplica a archivos tipo `tsk`. Tres valores posibles en el frontmatter:

| status | emoji | significado |
|---|---|---|
| `nueva` | 🌑 | disponible para uso temporal o sin proyecto asignado |
| `creciente` | 🌒 | proyecto en curso |
| `llena` | 🌕 | proyecto terminado, pendiente de documentar y archivar |

---

### Template de referencia
**Archivo:** `E:\University_vault_2026\_projects\tsk_tpl.md`
YAML base de todo archivo `tsk`:
```yaml
project: ""
date: 
status: nueva
```

---

### Archivos editados esta sesión

| Archivo | Cambio |
|---|---|
| `_projects\tsk_alx-rul.md` | `libre` → `nueva` |
| `_projects\tsk_alxgml.md` | `activo` → `creciente` |
| `_projects\tsk_alxhot.md` | `activo` → `creciente` |
| `_projects\tsk_alxrul.md` | `activo` → `creciente` |
| `_projects\tsk_krajo.md` | `activo` → `creciente` |
| `_projects\tsk_emergn.md` | sin YAML → `nueva` |
| `_projects\tsk_standb.md` | sin YAML → `creciente` |

---

### Estado al cierre
✅ Plugin instalado
✅ CSS generado y activo
✅ Prueba de funcionamiento exitosa
✅ Todos los `tsk` existentes migrados al nuevo sistema de status