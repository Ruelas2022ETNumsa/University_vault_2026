








```dataview
TABLE title, topic, status
FROM "semestres"
WHERE galaxy_body = "comet" AND subject = "ETN806" AND status = "pendiente"
SORT topic ASC
```








```dataview
TABLE galaxy_body, title
FROM "semestres"
WHERE subject = "ETN806" AND partial = 2
SORT galaxy_body ASC
```


```dataview
TABLE subject, galaxy_body, title
FROM "semestres"
WHERE status = "pendiente" OR status = "en-proceso"
SORT subject ASC
```






![[RENOMBRAR-30-05-2026 13.12.12.excalidraw#^frame=01]]




![[_app/Excalidraw/RENOMBRAR-30-05-2026 13.12.12.excalidraw.md#^BlXLPDwz|hhhh]]