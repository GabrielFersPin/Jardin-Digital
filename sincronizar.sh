#!/bin/bash

# 1. Cargar el entorno de Node/NVM para que Obsidian use la versión correcta
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"

# Intentar usar la versión v22 que es la que tienes en tu terminal
nvm use v22 --silent || nvm use default --silent

echo "🔄 Copiando notas desde tu Segundo Cerebro..."
# Sincronizamos las carpetas de forma exacta, borrando lo que ya no esté y excluyendo .git
rsync -a --delete --exclude='.git' --exclude='.obsidian' /home/gabriel/Documents/Segundo_Cerebro/ /home/gabriel/quartz/content/

echo "🚀 Subiendo a GitHub..."
# Cambiamos al directorio de Quartz por si acaso
cd /home/gabriel/quartz
npx quartz sync

echo "✅ ¡Listo! Página actualizada."
