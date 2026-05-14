#!/bin/bash

echo "🔄 Copiando notas desde tu Segundo Cerebro..."
# Sincronizamos las carpetas de forma exacta, borrando lo que ya no esté y excluyendo .git
rsync -a --delete --exclude='.git' --exclude='.obsidian' /home/gabriel/Documents/Segundo_Cerebro/ /home/gabriel/quartz/content/

echo "🚀 Subiendo a GitHub..."
# Cambiamos al directorio de Quartz por si acaso
cd /home/gabriel/quartz
npx quartz sync

echo "✅ ¡Listo! Página actualizada."
