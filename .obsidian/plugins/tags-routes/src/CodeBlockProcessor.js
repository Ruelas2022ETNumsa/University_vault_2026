// ============================================================
// src/util/CodeBlockProcessor.js
// Extraído de main.js — Sesión 2 (2026-05-14)
//
// Procesa bloques de código ```tagsroutes``` en las notas.
// Dependencias del scope global (definidas en main.js):
//   - DebugMsg           (src/util/util.ts)
//   - getLineTime        (src/util/util.ts)
//   - globalProgramControl (src/main.ts)
//
// Cuando util.ts sea extraído (Paso 4), actualizar este archivo
// para importar DebugMsg y getLineTime desde ./util.js
// ============================================================

// src/util/CodeBlockProcessor.ts
var import_obsidian5 = require("obsidian");
var pattern_tags_char = "#[0-9a-zA-Z\\u4e00-\\u9fa5/_-]";
var pattern_timeStamp = "\\d{4}-\\d{2}-\\d{2} *\\d{2}:\\d{2}:\\d{2}";
var tagRegEx = /\^tr-[a-z0-9]+$/;
var regex_TagsWithTimeStamp = new RegExp(`(?:(?<=\\s)|(?<=^))((?:${pattern_tags_char}+ *)+)(${pattern_timeStamp})?`, "gm");
var timeDurationRegex = /#\d+day/;
var performanceCount = class {
  constructor() {
    this.start = performance.now();
    this.startDatetime = (0, import_obsidian5.moment)(new Date()).format("YYYY-MM-DD HH:mm:ss");
  }
  getTimeCost() {
    this.end = performance.now();
    this.endDatetime = (0, import_obsidian5.moment)(new Date()).format("YYYY-MM-DD HH:mm:ss");
    const retStr = `Start at: ${this.startDatetime} - ${this.endDatetime}, execution: ${this.end - this.start} ms`;
    this.start = performance.now();
    this.startDatetime = (0, import_obsidian5.moment)(new Date()).format("YYYY-MM-DD HH:mm:ss");
    return retStr;
  }
};
var codeBlockProcessor = class {
  constructor(plugin) {
    this.plugin = plugin;
    this.codeBlockProcessor = this.codeBlockProcessor.bind(this);
  }
  getTimeDiffHour(start, end) {
    return (new Date(end).getTime() - new Date(start).getTime()) / (1e3 * 60 * 60);
  }
  async frontmatterTagProcessor(query) {
    const tag = query.value;
    const files = this.plugin.app.vault.getMarkdownFiles().filter((f) => this.plugin.view.testPathFilter(f.path));
    const matchingFiles = await Promise.all(files.map(async (file) => {
      var _a;
      const cache2 = this.plugin.app.metadataCache.getCache(file.path);
      if ((_a = cache2 == null ? void 0 : cache2.frontmatter) == null ? void 0 : _a.tags) {
        let tags = Array.isArray(cache2.frontmatter.tags) ? cache2.frontmatter.tags : [cache2.frontmatter.tags];
        if (tags.includes("tag-report")) {
          return null;
        }
        if (tags.some((t) => t.includes(tag))) {
          return file.path;
        }
      }
      return null;
    }));
    const result = matchingFiles.filter((path) => path !== null);
    const writeContent = `
# Total \`${result.length}\` notes with tag \`${tag}\` :
${result.map((v) => "- [[" + v.replace(/.md$/, "") + "]]").join("\n")}
`;
    return [writeContent];
  }
  async tagProcessor(query) {
    const term = query.value;
    const files = this.plugin.app.vault.getMarkdownFiles().filter((f) => this.plugin.view.testPathFilter(f.path));
    const arr = files.map(
      async (file) => {
        const content = await this.plugin.app.vault.cachedRead(file);
        const fmi = (0, import_obsidian5.getFrontMatterInfo)(content);
        if (fmi.exists && fmi.frontmatter.contains("tag-report")) {
          return [];
        }
        const paragraphs = content.split(/\n[\ ]*\n/).filter((line) => line.contains(term));
        if (paragraphs.length != 0) {
          var mmtime;
          var regstr = term + "[#a-zA-Z0-9\\-/_\u4E00-\u9FA5 ]* +(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})";
          var regex = new RegExp(regstr, "g");
          let updatedContent = content;
          let isUpdated = false;
          const retArr = paragraphs.map(
            (paragraph) => {
              const stripedParagraph = paragraph.replace(/<.*>/gm, "").replace(/```.*```/gm, "").replace(/#\d+day/gm, "");
              if (paragraph.length != stripedParagraph.length) {
              }
              regex.lastIndex = 0;
              let match = regex.exec(stripedParagraph);
              if (match) {
                mmtime = " Tag Time: " + match[1];
              } else {
                mmtime = " Created Time: " + (0, import_obsidian5.moment)(file.stat.ctime).format("YYYY-MM-DD HH:mm:ss");
              }
              let randomLinker = "";
              if (this.plugin.settings.enableParagraphLinker) {
                const tagMatch = paragraph.trimEnd().match(tagRegEx);
                if (tagMatch) {
                  randomLinker = tagMatch[0].substring(1);
                } else {
                  randomLinker = "tr-" + Math.random().toString(36).substr(2, 9);
                  let updatedLine = "";
                  if (paragraph.trimEnd().match(/\`\`\`/)) {
                    updatedLine = paragraph.trimEnd() + `
^${randomLinker}
`;
                  } else {
                    updatedLine = paragraph.trimEnd() + ` ^${randomLinker}
`;
                  }
                  updatedContent = updatedContent.replace(paragraph, updatedLine.trimEnd());
                  isUpdated = true;
                }
                randomLinker = `#^${randomLinker}`;
              }
              const regexp_local = new RegExp(regex_TagsWithTimeStamp.source, regex_TagsWithTimeStamp.flags);
              let matched_Tags_Timestamp_Group;
              let contentTimeString = mmtime;
              let retParagraph = "";
              while ((matched_Tags_Timestamp_Group = regexp_local.exec(stripedParagraph)) !== null) {
                let matched_Tags = matched_Tags_Timestamp_Group[1];
                const regexB = new RegExp(`${pattern_tags_char}+`, "gm");
                const matches = matched_Tags.match(regexB);
                retParagraph = paragraph.trimEnd() + "\n\n----\n [ *Tags:* " + (matches == null ? void 0 : matches.join(" ")) + " ]\n[ *" + contentTimeString + "* ]\n" + (this.plugin.settings.enableParagraphLinker ? `[ *From:* [[${file.path}${randomLinker}|${file.name.split(".")[0]}]] ]
` : `[ *From:* [[${file.path}|${file.name.split(".")[0]}]] ]
`);
              }
              return retParagraph;
            }
          );
          if (isUpdated) {
            await this.plugin.app.vault.modify(file, updatedContent);
            DebugMsg(4 /* DEBUG */, "file modified: ", file);
          }
          return retArr;
        } else {
          return [];
        }
      }
    );
    return arr;
  }
  /***
   * the all tag content within a time period
   */
  async timeDurationProcessor(query) {
    const queryDuration = Number(query.value.replace("#", "").replace("day", ""));
    const files = this.plugin.app.vault.getMarkdownFiles().filter((f) => this.plugin.view.testPathFilter(f.path));
    const arr = files.map(
      async (file) => {
        const content = await this.plugin.app.vault.cachedRead(file);
        const fmi = (0, import_obsidian5.getFrontMatterInfo)(content);
        if (fmi.exists && fmi.frontmatter.contains("tag-report")) {
          return [];
        }
        const paragraphs = content.split(/\n[\ ]*\n/);
        if (paragraphs.length != 0) {
          let updatedContent = content;
          let isUpdated = false;
          const retArr = paragraphs.map(
            //return the paragraph with information: "tags, tag/create time, from" appended.
            (paragraph) => {
              const stripedParagraph = paragraph.replace(/<.*>/gm, "").replace(/```.*```/gm, "").replace(/#\d+day/gm, "");
              if (paragraph.length != stripedParagraph.length) {
              }
              let matched_Tags_Timestamp_Group;
              let contentTimeString;
              let retParagraph = "";
              const regexp_local = new RegExp(regex_TagsWithTimeStamp.source, regex_TagsWithTimeStamp.flags);
              while ((matched_Tags_Timestamp_Group = regexp_local.exec(stripedParagraph)) !== null) {
                let matched_Timestamp = matched_Tags_Timestamp_Group[2] || "";
                let matched_Tags = matched_Tags_Timestamp_Group[1];
                let lineTime = "";
                if (matched_Timestamp !== "") {
                  contentTimeString = " Tag Time: " + matched_Tags_Timestamp_Group[2];
                  lineTime = matched_Tags_Timestamp_Group[2];
                } else {
                  lineTime = (0, import_obsidian5.moment)(file.stat.ctime).format("YYYY-MM-DD HH:mm:ss");
                  contentTimeString = " Created Time: " + lineTime;
                }
                let duration = this.getTimeDiffHour(lineTime, (0, import_obsidian5.moment)(new Date()).format("YYYY-MM-DD HH:mm:ss"));
                if (duration > 24 * queryDuration) {
                  continue;
                }
                let randomLinker = "";
                if (this.plugin.settings.enableParagraphLinker) {
                  const tagMatch = paragraph.trimEnd().match(tagRegEx);
                  if (tagMatch) {
                    randomLinker = tagMatch[0].substring(1);
                  } else {
                    randomLinker = "tr-" + Math.random().toString(36).substr(2, 9);
                    let updatedLine = "";
                    if (paragraph.trimEnd().match(/\`\`\`/)) {
                      updatedLine = paragraph.trimEnd() + `
^${randomLinker}
`;
                    } else {
                      updatedLine = paragraph.trimEnd() + ` ^${randomLinker}
`;
                    }
                    updatedContent = updatedContent.replace(paragraph, updatedLine.trimEnd());
                    isUpdated = true;
                  }
                  randomLinker = `#^${randomLinker}`;
                }
                const regexB = new RegExp(`${pattern_tags_char}+`, "gm");
                const matches = matched_Tags.match(regexB);
                retParagraph = paragraph.trimEnd() + "\n\n----\n [ *Tags:* " + (matches == null ? void 0 : matches.join(" ")) + " ]\n[ *" + contentTimeString + "* ]\n" + (this.plugin.settings.enableParagraphLinker ? `[ *From:* [[${file.path}${randomLinker}|${file.name.split(".")[0]}]] ]
` : `[ *From:* [[${file.path}|${file.name.split(".")[0]}]] ]
`);
              }
              return retParagraph;
            }
          );
          if (isUpdated) {
            await this.plugin.app.vault.modify(file, updatedContent);
            DebugMsg(4 /* DEBUG */, "file modified: ", file);
          }
          return retArr;
        } else {
          return [];
        }
      }
    );
    return arr;
  }
  writeMarkdownWrap(query, source, el, ctx) {
    if (query.type == "frontmatter_tag:") {
      this.writeMarkdown(query.type + query.value, source, el, ctx);
    } else {
      this.writeMarkdown(query.value, source, el, ctx);
    }
  }
  async writeMarkdown(term, source, el, ctx) {
    const markDownSource = source;
    if (globalProgramControl.useDiv) {
      import_obsidian5.MarkdownRenderer.render(
        this.plugin.app,
        markDownSource,
        el.createEl("div"),
        ctx.sourcePath,
        this.plugin.app.workspace.getActiveViewOfType(import_obsidian5.MarkdownView)
      );
    } else {
      const fileContent = `---
tags:
  - tag-report
---

\`\`\`tagsroutes
        ${term}
\`\`\`
*This file is automatically generated and will be overwritten.*
*Please do not edit this file to avoid losing your changes.*
`;
      const { vault } = this.plugin.app;
      const file = vault.getAbstractFileByPath(ctx.sourcePath);
      if (file instanceof import_obsidian5.TFile) {
        vault.modify(file, fileContent + markDownSource);
      }
    }
  }
  extractQueryKey(source) {
    let queryKey = { type: "", value: "", result: [] };
    if (source.contains("frontmatter_tag:")) {
      queryKey.type = "frontmatter_tag:";
      queryKey.value = source.replace(/frontmatter_tag:/, "").trim();
    } else {
      const regstr = `(${pattern_tags_char}*)`;
      const regex = new RegExp(regstr, "g");
      const match = source.match(regex);
      const term = (match == null ? void 0 : match[0]) || "#empty";
      const timeRegex = new RegExp(timeDurationRegex.source, timeDurationRegex.flags);
      const timeMatch = term.match(timeRegex);
      if (timeMatch) {
        queryKey.type = "time_duration:";
        queryKey.value = term;
      } else {
        queryKey.type = "tag:";
        queryKey.value = term;
      }
    }
    return queryKey;
  }
  getMarkdownContent(query) {
    if (query.type == "frontmatter_tag:")
      return query.result;
    const noteArr = query.result;
    const term = query.value;
    const markdownText = [];
    if (globalProgramControl.useGroup) {
      const tagMap = /* @__PURE__ */ new Map();
      const regex1 = new RegExp(`(?<= )${pattern_tags_char}+`, "g");
      noteArr.sort((b, a2) => getLineTime(a2) - getLineTime(b));
      for (let i = 0; i < noteArr.length; i++) {
        const matches = noteArr[i].replace(/[^]*Tags:/, "").replace(/<.*>/gm, "").replace(/```.*```/gm, "").match(regex1);
        try {
          matches == null ? void 0 : matches.forEach((m2) => {
            var _a;
            if (!tagMap.has(m2)) {
              tagMap.set(m2, new Array());
            }
            (_a = tagMap.get(m2)) == null ? void 0 : _a.push(noteArr[i]);
            if (!globalProgramControl.allowDuplicated) {
              throw "pushed";
            }
          });
        } catch (error) {
        }
      }
      markdownText.push("# Tag [" + term + "] total: `" + noteArr.length + "` records.");
      tagMap.forEach((content, tag) => {
        content.sort((a2, b) => getLineTime(a2) - getLineTime(b));
        markdownText.push(`# \\${tag} (${content.length})`);
        for (let i = 0; i < content.length; i++) {
          content[content.length - 1 - i] = content[content.length - 1 - i].replace(/^#/g, "###").replace(/\n#/g, "\n###");
          content[content.length - 1 - i] = "> [!info]+ " + (i + 1) + "\n> " + content[content.length - 1 - i].replace(/\n/g, "\n> ");
          markdownText.push("## " + (i + 1) + `
${content[content.length - 1 - i]}`);
        }
      });
    } else {
      noteArr.sort((a2, b) => getLineTime(a2) - getLineTime(b));
      markdownText.push("# Tag [" + term + "] total: `" + noteArr.length + "` records.");
      for (let i = 0; i < noteArr.length; i++) {
        noteArr[noteArr.length - 1 - i] = noteArr[noteArr.length - 1 - i].replace(/^#/g, "###").replace(/\n#/g, "\n###");
        noteArr[noteArr.length - 1 - i] = "> [!info]+ " + (i + 1) + "\n> " + noteArr[noteArr.length - 1 - i].replace(/\n/g, "\n> ");
        markdownText.push("## " + (i + 1) + `
${noteArr[noteArr.length - 1 - i]}`);
      }
    }
    return markdownText;
  }
  async codeBlockProcessor(source, el, ctx) {
    if (ctx.frontmatter.tags !== void 0) {
      return;
    }
    const query = this.extractQueryKey(source);
    const perf = new performanceCount();
    this.writeMarkdownWrap(query, '<br><div class="container-fluid"><div class="tg-alert"><b>PROCESSING...</b></div><small><em>The first time will be slow depending on vault size.</em></small></div>', el, ctx);
    switch (query.type) {
      case "frontmatter_tag:":
        query.result = await this.frontmatterTagProcessor(query);
        break;
      case "time_duration:":
        query.result = (await Promise.all(await this.timeDurationProcessor(query))).flat().filter((v) => v != "");
        break;
      case "tag:":
        query.result = (await Promise.all(await this.tagProcessor(query))).flat().filter((v) => v != "");
        break;
    }
    let executionTimeString;
    if (globalProgramControl.debugLevel == 4 /* DEBUG */) {
      executionTimeString = perf.getTimeCost();
    } else {
      executionTimeString = `Report refreshed at ${(0, import_obsidian5.moment)(new Date()).format("YYYY-MM-DD HH:mm:ss")} `;
    }
    const mc = "*" + executionTimeString + "*\n\n" + this.getMarkdownContent(query).filter((line) => line.trim() !== "").join("\n");
    this.writeMarkdownWrap(query, mc, el, ctx);
    return;
  }
};


// ============================================================
// EXPORTS
// ============================================================
module.exports = { codeBlockProcessor };
