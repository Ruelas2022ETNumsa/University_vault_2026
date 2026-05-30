```dataview
TABLE subject, galaxy_body, title
```









```dataview
TABLE title, topic, status
FROM "Semesters"
WHERE galaxy_body = "comet" AND subject = "ETN806" AND status = "pendiente"
SORT topic ASC
```








```dataview
TABLE galaxy_body, title
FROM "Semesters"
WHERE subject = "ETN806" AND partial = 2
SORT galaxy_body ASC
```


```dataview
TABLE subject, galaxy_body, title
FROM "Semesters"
WHERE status = "pendiente" OR status = "en-proceso"
SORT subject ASC
```




