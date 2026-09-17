---
tipo: dashboard-general
created: 2025-11-19
---

# 📊 Control de Estudio

## 🎯 Vista Global de Areas
```dataviewjs
// Agrupa notas por `area` y muestra estado, hito importante y contador de notas
const pages = dv.pages('').filter(p => p.area);
const areas = {};
for (const p of pages) {
  const a = p.area;
  if (!a) continue;
  if (!areas[a]) areas[a] = {count: 0, hito: null, estado: null};
  areas[a].count += 1;
  if (p['hito-importante']) areas[a].hito = p['hito-importante'];
  if (p.estado) areas[a].estado = p.estado;
}
dv.table(["Area","Estado","🎯 Próximo Hito","Notas"], Object.entries(areas).map(([k,v]) => [k, v.estado || "", v.hito || "", v.count]));
```

## 🔴 URGENTE: Temas para HOY
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "📚 Area",
  nivel-comprension as "Nivel",
  tiempo-repaso as "⏱️"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida", "permanente", "problema"), tipo_nota)
  AND area
  AND proxima-revision <= date(today)
SORT area ASC
```

## 🟡 Esta semana (próximos 7 días)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "Area",
  proxima-revision as "📅 Fecha",
  nivel-comprension as "Nivel"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida", "permanente", "problema"), tipo_nota)
  AND area
  AND proxima-revision > date(today)
  AND proxima-revision <= date(today) + dur(7 days)
SORT proxima-revision ASC
```

## 📚 Notas completas (listas para estudiar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  area as "Area",
  status as "Estado",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND area
  AND nivel-comprension
  AND proxima-revision
SORT proxima-revision ASC
```

## ⚠️ Notas incompletas (necesitan actualizar)
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  choice(area, "✅", "❌ Falta") as "Area",
  choice(nivel-comprension, "✅", "❌ Falta") as "Nivel",
  choice(proxima-revision, "✅", "❌ Falta") as "Próxima revisión"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND status = "🔴 Por procesar"
```

## 🔁 Notas esperando segunda revisión
```dataview
TABLE WITHOUT ID
  file.link as "Tema",
  status as "Estado",
  area as "Area",
  nivel-comprension as "Nivel",
  proxima-revision as "📅 Revisar"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida"), tipo_nota)
  AND status
  AND status != "🔴 Por procesar"
  AND status != "🎉 Completado / Archivado"
  AND proxima-revision
SORT proxima-revision ASC
```

## 📊 Estadísticas

- **Total notas técnicas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota)).length`
- **Notas completas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota) && p.area && p["nivel-comprension"] && p["proxima-revision"]).length`
- **Notas incompletas**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota) && p.status == "🔴 Por procesar").length`
- **Esperando segunda revisión**: `$= dv.pages('""').where(p => ["tecnica", "nota_estudio", "captura_rapida"].includes(p.tipo_nota) && p.status && p.status != "🔴 Por procesar" && p.status != "🎉 Completado / Archivado" && p["proxima-revision"]).length`
- **Temas dominados (✅/🎯)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "✅" || p["nivel-comprension"] == "🎯").length`
- **En progreso (💡)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "💡").length`
- **Necesitan atención (❓/🤔)**: `$= dv.pages('""').where(p => p["nivel-comprension"] == "❓" || p["nivel-comprension"] == "🤔").length`

## 🧭 Cuellos de botella del sistema

### 🧹 Capturas que necesitan procesamiento
```dataview
TABLE WITHOUT ID
  file.link as "Nota",
  choice(area, area, asignatura) as "Area",
  choice(proxima-revision, proxima-revision, proxima_revision) as "Fecha"
FROM ""
WHERE contains(list("captura_rapida", "clase"), tipo_nota)
  AND (status = "🔴 Por procesar" OR procesamiento = "CAPTURA-RAPIDA" OR !area)
SORT file.ctime ASC
LIMIT 20
```

### 🧪 Notas sin aplicación o recuperación registrada
```dataview
TABLE WITHOUT ID
  file.link as "Nota",
  choice(area, area, asignatura) as "Area",
  choice(nivel-comprension, nivel-comprension, nivel_comprension) as "Nivel",
  choice(resultado-repaso, resultado-repaso, "Pendiente") as "Resultado"
FROM ""
WHERE contains(list("tecnica", "nota_estudio", "captura_rapida", "permanente", "problema"), tipo_nota)
  AND (!resultado-repaso OR !file.outlinks OR length(file.outlinks) = 0)
  AND status != "🎉 Completado / Archivado"
SORT file.mtime DESC
LIMIT 20
```

### 🔁 Revisiones difíciles o fallidas
```dataview
TABLE WITHOUT ID
  file.link as "Nota",
  resultado-repaso as "Resultado",
  veces-revisado as "Repasos",
  choice(proxima-revision, proxima-revision, proxima_revision) as "Próxima revisión"
FROM ""
WHERE resultado-repaso = "fallado" OR resultado-repaso = "dificil"
SORT choice(proxima-revision, proxima_revision, date("9999-12-31")) ASC
```

---

## 🗓️ Por Area

```dataviewjs
const tiposNota = ["tecnica", "nota_estudio", "captura_rapida"];
const estadoPorProcesar = "🔴 Por procesar";
const estadoArchivado = "🎉 Completado / Archivado";
const paginas = dv.pages("").where(p => tiposNota.includes(p.tipo_nota) && p.area);
const areas = new Map();

for (const pagina of paginas) {
  const area = String(pagina.area);
  if (!areas.has(area)) {
    areas.set(area, {
      total: 0,
      porProcesar: 0,
      segundaRevision: 0,
      proximaRevision: null
    });
  }

  const resumen = areas.get(area);
  resumen.total += 1;

  if (pagina.status === estadoPorProcesar) {
    resumen.porProcesar += 1;
  }

  if (
    pagina.status &&
    pagina.status !== estadoPorProcesar &&
    pagina.status !== estadoArchivado &&
    pagina["proxima-revision"]
  ) {
    resumen.segundaRevision += 1;
  }

  const fecha = pagina["proxima-revision"];
  if (fecha && (!resumen.proximaRevision || fecha < resumen.proximaRevision)) {
    resumen.proximaRevision = fecha;
  }
}

const filas = [...areas.entries()]
  .sort(([areaA], [areaB]) => areaA.localeCompare(areaB))
  .map(([area, resumen]) => [
    area,
    resumen.total,
    resumen.porProcesar,
    resumen.segundaRevision,
    resumen.proximaRevision || "Sin fecha"
  ]);

dv.table(
  ["Area", "Total", "Por procesar", "Segunda revisión", "Próxima fecha"],
  filas
);
```

---


---


