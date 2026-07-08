



rearaer %%> prueba%%

las configuraciones te las entrego en forma de texto ojo si es una extraccion%%> img:[[void-07-07-2026_20-17-39.png]] %%
literal si solo una aclaracion en cada opcion la utloma [] es como se puede%%> img:[[doodle_20260707_202126.png]] %%
configurar, [1/0] on/off, [slider] para distintos valores a escoger, [valor x/valor y] entre dos o mas valores,%%> img:[[doodle_20260707_202044.png]] %%
[text=MMM] texto escrito en la configuracion solo esta "MMM" sin `text=`,  %%> img:[[doodle_20260707_202211.png]] %%
[button=nombre del boton] solo aparece "nombre del boton" no "button=".%%> img:[[void-07-07-2026_20-19-07.png]] %%

# Cornell Marginalia Sdfgdfgdfgdfgettingsdfg> img:[[doodle_20260707_202242.png]] %%

## 🎨 Appearance & Rendering

### Responsive Marginalia (Auto-Collapse) [1/0]
OPTIONAL: Automatically move marginalia inside the text when the%%> img:[[doodle_20260707_202300.png]] %%
note pane is too narrow (e.g. when you open the sidebar).

### Responsive Threshold (px) [Slider]
Set the width at which marginalia collapses into the text.
(Requires Auto-Collapse to be ON).

### Adaptive Width (Theme Compatibility) [1/0]
🧠 Auto-calculates margin width based on empty screen space. Turn
ON if you are having problems with your current theme to prevent overlap.

### Margin Alignment [Left/right]

### Margin Width (%) [slider]

### Margin Distance (Offset) [slider]
Adjust how close or far the marginalia sits from the main
text. Higher values push it outwards, lower values pull it
inwards.

### Font Size [text=0.85em]

### Font Family [text=inherit]

### Enable in Reading View [1/0]
Shows marginalia in reading mode. Turn this off if you prefer a clean
view.

### Extract Highlights [1/0]
OPTIONAL: Include standard text highlights (==text==) in the
Explorer and Pinboard.

### Blur Explanatory Marginalias [1/0]
🧠 Active Recall: Blurs regular marginalias that share a line with a
flashcard, preventing spoilers.


##🏷️ Color Tags

- Tag 1 [text=!] [seleccion de color valores RGB] [button=eliminar]
- Tag 2 [text=?] [seleccion de color valores RGB] [button=eliminar]
- Tag 3 [text=X-] [seleccion de color valores RGB] [button=eliminar]
- Tag 4 [text=V-] [seleccion de color valores RGB] [button=eliminar]
- [button=Add Tag ]

##📁 Structural Box Colors

Asigna colores EXCLUSIVAMENTE a los recuadros de los Hilos Semánticos
(ej: #abuelo). Esto NO alterará el color de tus marginalias en el texto.

[button=Add Box Color]

##✅ Task Management

### Auto-Delete Completed Tasks [1/0]
When you check a marginalia task (- [x]), it will be permanentlyasdasd%%> img:[[doodle_20260707_202326.png]] %%
deleted from the Markdown file to keep your vault clean.

### TaskNotes HTTP API Integration [1/0]
Shows a button on task marginalias to send them directly to the
TaskNotes plugin.

##📁 File & Output Management

### Omni-Capture Default Folder [text=Example: 00_Inbox]
Folder where new marginalia files will be
created (leave empty for root).

### Omni-Capture Template
[text=
%%> {{text}} %%
{{citation}}
{{image}}

---
]
Define the output format for your captures.
Use {{text}}, {{citation}}, and {{image}}. Supports
Templater (<% %>). If you want to use Flashcard
mode, remember to include ';;' inside your text template.

### Zettelkasten Folder [text=Zettelkasten]
Where should your ZK notes be created?
(Leave empty for root).

### Zettelkasten Template Path [text=]
Optional: Path to a markdown file to use as a
template (e.g., Templates/ZK.md). Supports
{{title}}, {{date}}, {{time}}.

### Doodles Folder[text=Marginalia Attachments]
Where should your hand-drawn images
be saved? (Leave empty for root).

### Evidence Boards Folder [text=Evidence Boards]
Where should your Canvas files be exported?

### Pinboards Folder [textPinboards]
Where should your exported Pinboard
Markdown files go?

### Pinboards Template Path [text=]
Optional: Path to a markdown file to use as a
template for exported Boards.

### Pinboards Item Template Path [text=]
Optional: Template for each individual
marginalia in the board. Supports {{text}},
{{citation}}, and {{source_note}}.

### Canvas Item Template Path [text= ]
Optional: Template for the main marginalia
node in the Evidence Board. Supports {{text}}
and {{source_note}}.

### ✨ Clean Exports (Remove Tags) [1/0]
Automatically strip #tags from notes when exporting to Pinboard,
Canvas, or Dragging to a note.

### ✨ Clean Exports (Remove Block IDs) [1/0]
Automatically strip ^block-ids from your notes when exporting.

### Drag & Drop Template (To Note)
[text=
- {{text}} {{source_note}}
]

Format used when you drag a Semantic Thread
box directly into a Markdown note. Supports
{{text}}, {{citation}}, {{time}} and {{source_note}}.

## ⚙️ Advanced & Exclusions

### Show Syntax in Source Mode [1/0]
If enabled, Cornell Notes will show as raw Markdown syntax when
using Source Mode, instead of rendering visual blocks.

### Ignored Folders [text=Templates]
Comma-separated list of folders to completely ignore.

### Ignored Folders for Highlights [text=Excalidraw]
Comma-separated list of folders to ignore ONLY
for highlights (e.g., Excalidraw, Templates).

### Ignored Highlight Texts
[text=
⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠
]

Comma-separated list of exact texts or fragments
to ignore (e.g., Switch to EXCALIDRAW VIEW).


### 🔗 Semantic Stitching UI [1/0]
When connecting (stitching) notes, ask for a semantic
reason (e.g. "miden lo mismo").

## 🛠️ Addons & Modules

### Gamification & User Profile [1/0]
Turn your marginalia into a game! Earn XP, level up, and customize
your profile sidebar.

### Custom Explorer Background [1/0]
Add a beautiful background image to your Marginalia Explorer.

### 🌱 Time Machine & Rhizome [1/0]
Explore your marginaliae on a chronological, full-screen interactive
canvas with spaced repetition.

### Pdf Doodle & Harvest [1/0]
Enable temporary drawing mode on PDFs.

### Super Doodle 🎨 [1/0]
Transform Zen Doodle into an adjustable-size canvas with panoramic
navigation, colors, and an advanced selection tool.

### 🧠 Blurting Mode (1-3-7) [1/0]
Turn your Marginalia Explorer into a Spaced Repetition study deck.

### 🍅 Margidoro Engine [1/0]
Knowledge-aware Pomodoro timer. Tracks your marginalias during
study sessions and schedules reviews.

### Anki Advanced Sync [1/0]
Syncs marginalias to Anki with bidirectional support, native images,
and PDF++ crops.

### 🔍 Zoom & Pan Doodles [1/0]
Haz clic en cualquier imagen o doodle en tus marginalias para
expandirla a pantalla completa con controles de zoom y paneo.

### 🚀 Dashboard:Smart Study [1/0]
Linear calendar, routines, subjects, and dynamic spaced review.

### Cornell Board 🌌 [1/0]
Activate an infinite, freeform canvas to drag, connect, and visually
materialize marginalias.