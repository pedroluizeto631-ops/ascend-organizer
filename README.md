# 🚀 Ascend Organizer

Um organizador automático de arquivos desenvolvido com Python e interface moderna utilizando CustomTkinter.

O sistema organiza automaticamente arquivos da pasta Downloads em categorias específicas com base em suas extensões.

---

# ✨ Preview

## Funcionalidades

✅ Organização automática de arquivos
✅ Interface gráfica moderna
✅ Sistema de logs
✅ Configuração via JSON
✅ Arquitetura modular
✅ Tema dark moderno
✅ Criação automática de pastas
✅ Estrutura profissional de projeto

---

# 📂 Estrutura do Projeto

```bash id="rd0evj"
ascend-organizer/
│
├── assets/
├── logs/
├── config/
│   └── config.json
│
├── core/
│   ├── organizer.py
│   ├── categories.py
│   └── logger.py
│
├── ui/
│   ├── components.py
│   └── main_window.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 🧠 Como Funciona

O sistema:

1. Lê todos os arquivos da pasta Downloads
2. Identifica a extensão de cada arquivo
3. Consulta as categorias definidas no `config.json`
4. Cria automaticamente as pastas necessárias
5. Move os arquivos para suas respectivas categorias
6. Registra todas as ações em logs

---

# ⚙️ Configuração

O arquivo:

```bash id="48ui9x"
config/config.json
```

permite personalizar:

* categorias
* tema
* monitoramento
* configurações futuras

---

## Exemplo

```json id="7zwjlwm"
{
  "tema": "dark",
  "monitorar_downloads": true,
  "mostrar_logs": true,
  "pastas": {
    ".png": "Imagens",
    ".jpg": "Imagens",
    ".mp4": "Videos",
    ".pdf": "PDFs"
  }
}
```

---

# 🖥️ Tecnologias Utilizadas

* Python
* CustomTkinter
* Pathlib
* JSON
* Shutil
* Datetime

---

# 📦 Instalação

## Clone o repositório

```bash id="w1mjlwm"
git clone https://github.com/seuusuario/ascend-organizer.git
```

---

## Entre na pasta

```bash id="7s9jlwm"
cd ascend-organizer
```

---

## Instale as dependências

```bash id="qqjlwm"
pip install -r requirements.txt
```

---

# ▶️ Executando o Projeto

```bash id="jlwm31"
python main.py
```

---

# 📜 Sistema de Logs

Todas as ações são registradas automaticamente em:

```bash id="jlwm32"
logs/organizer.log
```

Exemplo:

```txt id="jlwm33"
[29/05/2026 03:14:20] foto.png movido para Imagens
```

---

# 🧩 Arquitetura do Projeto

O sistema foi desenvolvido utilizando arquitetura modular.

## Separação de responsabilidades

### core/

Responsável pela lógica do sistema.

### ui/

Responsável pela interface gráfica.

### config/

Responsável pelas configurações externas.

### logs/

Responsável pelos registros do sistema.

---

# 🔥 Funcionalidades Futuras

* Monitoramento em tempo real
* Dashboard visual
* Sistema de notificações
* Organização inteligente
* Tema customizável
* Exportação de relatórios
* Executável `.exe`
* Instalador automático

---

# 📚 Conceitos Aplicados

Durante o desenvolvimento foram utilizados:

* Modularização
* Orientação a Objetos
* Manipulação de Arquivos
* Tratamento de Erros
* Interface Gráfica
* Componentização
* Arquitetura de Software
* Logs
* Automação

---

# 👨‍💻 Autor

Desenvolvido por Luizeto 🚀
