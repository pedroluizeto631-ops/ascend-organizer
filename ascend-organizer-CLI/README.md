
# 🚀 Ascend Organizer CLI

Um organizador automático de arquivos desenvolvido em Python com interface interativa no terminal do Windows.

O sistema organiza automaticamente os arquivos da pasta Downloads utilizando menus navegáveis com setinhas ↑ ↓ diretamente no CMD, PowerShell ou Windows Terminal.

---

# ✨ Funcionalidades

✅ Organização automática de arquivos
✅ Interface interativa no terminal
✅ Navegação com setinhas ↑ ↓
✅ Estrutura visual em árvore
✅ Sistema de logs
✅ Configuração via JSON
✅ Criação automática de pastas
✅ Arquitetura modular
✅ Compatível com CMD do Windows

---

# 🖥️ Preview

```txt
╭────────────────────────────╮
│     ASCEND ORGANIZER       │
╰────────────────────────────╯

❯ 📂 Organizar Downloads
  📜 Ver Logs
  ❌ Sair
```

---

# 📂 Estrutura Visual

Após organizar os arquivos:

```txt
📂 Downloads
├── 📁 Imagens
│   ├── foto.png
│   ├── wallpaper.jpg
│
├── 📁 Videos
│   ├── aula.mp4
│
└── 📁 PDFs
    ├── ebook.pdf
```

---

# 📁 Estrutura do Projeto

```bash
ascend-organizer-CLI/
│
├── core/
│   ├── __init__.py
│   ├── organizer.py
│   ├── logger.py
│   └── categories.py
│
├── ui/
│   ├── __init__.py
│   ├── menu.py
│   └── tree_view.py
│
├── config/
│   └── config.json
│
├── logs/
│   └── organizer.log
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🧠 Como Funciona

O sistema:

1. Lê os arquivos da pasta Downloads
2. Identifica a extensão de cada arquivo
3. Consulta o `config.json`
4. Cria as pastas automaticamente
5. Move os arquivos para suas categorias
6. Registra logs do sistema
7. Exibe a estrutura final no terminal

---

# ⚙️ Configuração

Arquivo:

```bash
config/config.json
```

Exemplo:

```json
{
  "tema": "dark",

  "mostrar_logs": true,

  "monitorar_downloads": true,

  "pastas": {

    ".png": "Imagens",
    ".jpg": "Imagens",
    ".jpeg": "Imagens",

    ".mp4": "Videos",
    ".mkv": "Videos",

    ".pdf": "PDFs",

    ".mp3": "Musicas",

    ".zip": "Compactados",

    ".exe": "Programas"
  }
}
```

---

# 📦 Tecnologias Utilizadas

* Python
* Rich
* Questionary
* Pathlib
* JSON
* Shutil
* Datetime

---

# 📥 Instalação

## Clone o repositório

```bash
git clone https://github.com/seuusuario/ascend-organizer-CLI.git
```

---

# 📂 Entre na pasta do projeto

```bash
cd ascend-organizer-CLI
```

---

# 📦 Instale as dependências

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando no Terminal do Windows

## Abra o CMD

Pressione:

```txt
WIN + R
```

Digite:

```txt
cmd
```

---

# Vá até a pasta do projeto

Exemplo:

```bash
cd Desktop\meu-portfolio\ascend-organizer-CLI
```

---

# Execute o sistema

```bash
python main.py
```

---

# 🎮 Controles

| Tecla    | Função         |
| -------- | -------------- |
| ↑ ↓      | Navegar        |
| ENTER    | Selecionar     |
| CTRL + C | Fechar sistema |

---

# 📜 Sistema de Logs

Todos os logs ficam em:

```bash
logs/organizer.log
```

Exemplo:

```txt
[29/05/2026 03:14:20] foto.png movido para Imagens
```

---

# 🌳 Estrutura em Árvore

O sistema exibe automaticamente uma árvore visual após organizar os arquivos.

Exemplo:

```txt
📂 Downloads
├── 📁 Imagens
│   ├── foto.png
│   └── wallpaper.jpg
│
├── 📁 Videos
│   └── aula.mp4
│
└── 📁 PDFs
    └── ebook.pdf
```

---

# 🧩 Arquitetura do Projeto

## core/

Responsável pela lógica principal.

### organizer.py

Organização dos arquivos.

### logger.py

Sistema de logs.

### categories.py

Leitura do JSON.

---

## ui/

Responsável pela interface do terminal.

### menu.py

Menu interativo.

### tree_view.py

Visualização em árvore.

---

# 🚀 Funcionalidades Futuras

* Monitoramento em tempo real
* Dashboard no terminal
* Barra de progresso
* Tema cyberpunk
* Estatísticas do sistema
* Executável `.exe`
* Instalação automática

---

# 📚 Conceitos Aplicados

* Modularização
* Interface TUI
* Manipulação de Arquivos
* Logs
* JSON
* Automação
* Arquitetura de Software
* Terminal Interativo
* Estrutura em Árvore
* Tratamento de Erros

---

# 👨‍💻 Autor

Desenvolvido por Luizeto 🚀
