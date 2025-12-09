# PVQD Presentation Documentation

This directory contains a Beamer presentation about Projected Variational Quantum Dynamics (PVQD) implemented in LaTeX.

## Overview

The presentation covers the concept, formulation, and code implementation of PVQD (Projected Variational Quantum Dynamics), a variational method for simulating quantum time evolution on NISQ (Noisy Intermediate-Scale Quantum) devices.

## Files

- `slides.tex` - Main Beamer presentation source file
- `code_images/` - Directory containing code screenshots used in the presentation
  - `circuit.png` - Ansatz circuit implementation
  - `config.png` - Configuration parameters
  - `hamiltonian.png` - Hamiltonian definition
  - `ibm_backend.png` - IBM backend integration
  - `main.py` - Main pipeline
  - `primitives.png` - Primitive operations
  - `pvqd_solver.png` - PVQD solver implementation
  - `results.png` - Results analysis

## Presentation Structure

The presentation is organized into the following sections:

1. **Motivation** - Why PVQD is needed for NISQ devices
2. **PVQD — General Idea** - Overview of temporal evolution and variational states
3. **Formulation** - Mathematical equations and components of PVQD
4. **Code Architecture** - Detailed walkthrough of the implementation modules
5. **Conclusion** - Summary and key takeaways

## Key Topics Covered

### Motivation
- Computational difficulty of simulating quantum time evolution
- Limitations of NISQ devices with deep circuits
- Need for efficient variational methods
- PVQD as a projection method into accessible variational subspace

### PVQD Formulation
- Temporal evolution equation: $\ket{\psi(t+\Delta t)} = e^{-iH\Delta t}\ket{\psi(t)}$
- Variational state: $\ket{\psi(\theta(t))}$
- PVQD equations: $M \dot{\theta} = C$
- Components:
  - $M_{ij} = \Re(\braket{\partial_i\psi | \partial_j\psi})$ - Geometry of variational space
  - $C_i = \Im(\matrixel{\partial_i\psi}{H}{\psi})$ - Hamiltonian effect in variational direction
- Parameter update: $\dot{\theta} = M^{-1}C$ and $\theta(t+\Delta t) = \theta(t) + \Delta t \,\dot{\theta}$

### Code Architecture
The presentation includes code screenshots for:
- `config.py` - Simulation parameters
- `hamiltonian.py` - Hamiltonian definition
- `circuit.py` - Variational ansatz
- `pvqd_solver.py` - PVQD implementation
- `main.py` - Complete pipeline
- `results.py` - Analysis and plots
- `primitives.py` - Primitive operations
- `ibm_backend.py` - IBM backend integration

## How to Compile

### Prerequisites

Install LaTeX and required packages:

**Ubuntu/Debian:**
```bash
sudo apt-get install texlive-full
```

**Fedora:**
```bash
sudo dnf install texlive-scheme-full
```

**macOS (with Homebrew):**
```bash
brew install --cask mactex
```

### Compilation

To compile the PDF from the `.tex` file:

```bash
cd presentation
pdflatex slides.tex
pdflatex slides.tex  # Run twice for correct references
```

Or use automatic compilation:

```bash
pdflatex -interaction=nonstopmode slides.tex
```

**Note:** The presentation currently uses Portuguese language settings. To compile in English, you would need to change `\usepackage[brazil]{babel}` to `\usepackage[english]{babel}` in `slides.tex` and translate the content.

## Customization

### Changing the Theme

In `slides.tex`, line 3, you can change the theme:

```latex
\usetheme{Madrid}  % Options: default, Berlin, Warsaw, Madrid, etc.
```

### Changing Colors

Line 3, change the color theme:

```latex
\usecolortheme{default}  % Options: whale, seahorse, dolphin, etc.
```

### Adding Figures

1. Place your images in the `presentation/` directory
2. Use the `\includegraphics` command:

```latex
\includegraphics[width=0.7\textwidth]{figure_name.png}
```

## Template Features

The presentation template includes:

- ✅ Title slide
- ✅ Automatic table of contents
- ✅ Multiple sections
- ✅ Slides with lists
- ✅ Slides with equations
- ✅ Slides with blocks (normal, alert, example)
- ✅ Slides with columns
- ✅ Slides with code screenshots
- ✅ Slides with figures
- ✅ Conclusion slide
- ✅ Thank you slide

## Tips

1. **Aspect Ratio**: The template uses 16:9. For 4:3, change the first line to `\documentclass{beamer}`

2. **Language**: Currently configured for Portuguese (Brazil). To switch to English:
   - Change `\usepackage[brazil]{babel}` to `\usepackage[english]{babel}`
   - Translate all text content in the slides

3. **Code**: The presentation includes code screenshots. To update them, regenerate the images in the `code_images/` directory.

4. **References**: If using `\cite{}`, add a bibliography section and run `bibtex slides` before the second `pdflatex`

## Build Artifacts

The following files are generated during compilation and are excluded from version control (see `.gitignore`):

- `*.aux`, `*.log`, `*.nav`, `*.out`, `*.snm`, `*.toc`, `*.vrb`
- `_minted-slides/` directory
- `texput.log`

Only source files (`slides.tex`, `README.md`, and images) are tracked in the repository.

## Example Usage

1. Edit `slides.tex` with your content
2. Update code images in `code_images/` if needed
3. Compile with `pdflatex slides.tex` (run twice)
4. Open the generated `slides.pdf` file
