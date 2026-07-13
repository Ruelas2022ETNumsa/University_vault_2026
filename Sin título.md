```dataviewjs
const response = await fetch("https://api.wolframalpha.com/v2/query?input=2%2B2&appid=A3WL4X56LG&output=json");
const data = await response.json();
dv.paragraph(JSON.stringify(data).slice(0, 200));
```
