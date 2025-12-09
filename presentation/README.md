# Apresentação em Beamer

Este diretório contém um modelo de apresentação em LaTeX usando Beamer.

## Arquivos

- `slides.tex` - Modelo de apresentação em Beamer

## Como Compilar

### Pré-requisitos

Instale o LaTeX e os pacotes necessários:

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**Fedora:**
```bash
sudo dnf install texlive-scheme-full
```

**macOS (com Homebrew):**
```bash
brew install --cask mactex
```

### Compilação

Para compilar o PDF a partir do arquivo `.tex`:

```bash
cd presentation
pdflatex slides.tex
pdflatex slides.tex  # Execute duas vezes para referências corretas
```

Ou use o script de compilação automática:

```bash
pdflatex -interaction=nonstopmode slides.tex
```

## Personalização

### Mudar o Tema

No arquivo `slides.tex`, linha 4, você pode trocar o tema:

```latex
\usetheme{Madrid}  % Opções: default, Berlin, Warsaw, Madrid, etc.
```

### Mudar as Cores

Linha 5, troque o tema de cores:

```latex
\usecolortheme{default}  % Opções: whale, seahorse, dolphin, etc.
```

### Adicionar Figuras

1. Coloque suas imagens na pasta `presentation/`
2. Descomente e modifique a linha no slide de figura:

```latex
\includegraphics[width=0.7\textwidth]{nome_da_figura.png}
```

## Estrutura do Template

O template inclui:

- ✅ Slide de título
- ✅ Sumário automático
- ✅ Múltiplas seções
- ✅ Slides com listas
- ✅ Slides com equações
- ✅ Slides com blocos (normal, alerta, exemplo)
- ✅ Slides com colunas
- ✅ Slide com código
- ✅ Slide com figura
- ✅ Slide de conclusão
- ✅ Slide de perguntas

## Dicas

1. **Aspect Ratio**: O template usa 16:9. Para 4:3, mude a primeira linha para `\documentclass{beamer}`

2. **Idioma**: Configurado para português. Para inglês, mude `\usepackage[portuguese]{babel}` para `\usepackage[english]{babel}`

3. **Código**: O template inclui suporte para código Python. Para outras linguagens, ajuste `language=Python` no `\lstset`

4. **Referências**: Se usar `\cite{}`, adicione uma seção de bibliografia e execute `bibtex slides` antes do segundo `pdflatex`

## Exemplo de Uso

1. Edite `slides.tex` com seu conteúdo
2. Compile com `pdflatex slides.tex` (duas vezes)
3. Abra o arquivo `slides.pdf` gerado
