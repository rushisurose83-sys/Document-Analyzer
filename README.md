# ⚡ DocuParse Edge: Local-First AI Document Pipeline

An entirely offline, object-oriented text extraction and AI inference pipeline. This system leverages local Large Language Models (LLMs) to parse, analyze, and extract structured insights from compiled binaries (PDFs) and text documents without sending any data to the cloud.

## 🧠 Architecture Overview
This project demonstrates a zero-network Edge AI approach to document processing. By keeping inference local, it ensures strict data privacy, zero API latency, and reliable offline execution.

* **Smart Routing Engine:** Automatically detects file extensions (`.txt`, `.pdf`) and routes them to the appropriate extraction method.
* **Binary Extraction:** Utilizes `pypdf` to strip text from compiled PDFs.
* **Local AI Inference:** Integrates with the `ollama` Python bridge to pass extracted context directly to a locally hosted Llama3 model.

## 🛠️ Tech Stack
* **Language:** Python 3
* **AI Engine:** Ollama (Llama 3 - 8B Parameters)
* **Libraries:** `pypdf`, `ollama`
* **Design Pattern:** Object-Oriented Programming (OOP)

## 🚀 Quick Start / Installation

**1. Clone the repository and navigate to the directory:**
```bash
git clone [https://github.com/rushisurose83-sys/Offline-AI-PDF-Analyzer.git](https://github.com/rushisurose83-sys/Offline-AI-PDF-Analyzer.git)
cd Offline-AI-PDF-Analyzer