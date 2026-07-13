<%*
// ─── CONFIGURACIÓN ───────────────────────────────────────────────
const APP_ID = "A3WL4X56LG";
const ASSETS_FOLDER = "_assets";

// ─── SELECCIÓN ───────────────────────────────────────────────────
const selection = tp.file.selection();
if (!selection || selection.trim() === "") {
    new Notice("⚠️ Seleccioná una expresión antes de ejecutar el template.");
    return;
}
const expression = selection.trim();

// ─── LLAMADA A WA FULL API ────────────────────────────────────────
let resultText = "(sin resultado)";
let plotUrl = null;

try {
    const url = `https://api.wolframalpha.com/v2/query?input=${encodeURIComponent(expression)}&appid=${APP_ID}&output=json&podstate=Step-by-step+solution`;
    const response = await fetch(url);
    const data = await response.json();

    if (!data.queryresult.success) {
        new Notice("⚠️ WA no pudo interpretar la expresión.");
        return;
    }

    const pods = data.queryresult.pods;

    // Extraer resultado — buscar pod Result o Primary
    const resultPod = pods.find(p => p.id === "Result" || p.primary === true);
    if (resultPod?.subpods?.[0]?.plaintext) {
        resultText = resultPod.subpods[0].plaintext;
    }

    // Extraer URL de gráfica — buscar pod Plot
    const plotPod = pods.find(p => p.id === "Plot" || p.title?.toLowerCase().includes("plot"));
    if (plotPod?.subpods?.[0]?.img?.src) {
        plotUrl = plotPod.subpods[0].img.src;
    }

} catch (err) {
    new Notice("❌ Error al conectar con Wolfram Alpha: " + err.message);
    return;
}

// ─── DESCARGAR Y GUARDAR IMAGEN ───────────────────────────────────
let imageLink = null;

if (plotUrl) {
    try {
        // Calcular número siguiente para evitar sobreescritura
        const existingFiles = app.vault.getFiles()
            .filter(f => f.path.startsWith(ASSETS_FOLDER + "/ima-"))
            .map(f => {
                const match = f.name.match(/ima-(\d+)\.png/);
                return match ? parseInt(match[1]) : 0;
            });
        const nextN = existingFiles.length > 0 ? Math.max(...existingFiles) + 1 : 1;
        const imageName = `ima-${nextN}.png`;
        const imagePath = `${ASSETS_FOLDER}/${imageName}`;

        // Descargar imagen
        const imgResponse = await fetch(plotUrl);
        const arrayBuffer = await imgResponse.arrayBuffer();
        await app.vault.createBinary(imagePath, arrayBuffer);

        imageLink = `![[${imageName}]]`;
        new Notice(`✅ Imagen guardada: ${imageName}`);

    } catch (err) {
        new Notice("⚠️ No se pudo guardar la imagen: " + err.message);
        imageLink = `> *(imagen no disponible: ${err.message})*`;
    }
}

// ─── CONSTRUIR BLOQUE DE SALIDA ───────────────────────────────────
const imageBlock = imageLink
    ? imageLink
    : "> *(sin gráfica disponible)*";

const output = `
**WA:** ${resultText}
${imageBlock}

\`\`\`
Resolvé paso a paso sin ejercicio adicional (MODO 3):
${expression}
Si aplica, graficá usando Desmos o TikZJax.
\`\`\`
`;

tR += output;
%>
