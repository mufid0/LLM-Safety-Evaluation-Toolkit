# 🛡️ LLM Safety Evaluation & Alignment Toolkit

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Framework](https://img.shields.io/badge/Transformers-HuggingFace-yellow)
![Focus](https://img.shields.io/badge/Focus-AI%20Safety-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🚀 Overview

This project presents a **structured evaluation framework for Large Language Models (LLMs)**, focusing on **safety, alignment, and robustness**.

It benchmarks models across:

* Hallucination (factual correctness)
* Adversarial robustness (unsafe prompts)
* Bias across demographic variations
* Refusal behavior
* Response quality

> The goal is to **quantify trustworthiness of LLM outputs** using a reproducible evaluation pipeline.

---

## 🧠 Key Highlights

* Built a **hybrid evaluation dataset (120+ prompts)** combining synthetic data and benchmark datasets like TruthfulQA
* Designed a **multi-metric scoring system** for LLM safety evaluation
* Implemented **embedding-based bias detection**
* Developed a **modular evaluation pipeline (`src/`)** for scalability
* Benchmarked multiple transformer-based models with structured comparison

---

## 📊 Dataset

### 🔹 Synthetic Prompts

Designed to test:

* Factual correctness
* Misleading claims (hallucination detection)
* Harmful/unsafe prompts
* Logical reasoning

### 🔹 Benchmark Dataset

* Inspired by TruthfulQA

📌 **Total Dataset Size:** 120–140 prompts

---

## 🧪 Evaluation Metrics

| Metric                | Description                                     |
| --------------------- | ----------------------------------------------- |
| **Factual Score**     | Semantic similarity with reference answers      |
| **Adversarial Score** | Detects unsafe or harmful responses             |
| **Bias Score**        | Measures consistency across demographic prompts |
| **Refusal Score**     | Evaluates safe refusal behavior                 |
| **Final Score**       | Weighted composite safety score                 |

---

## 🤖 Models Evaluated

* GPT-2
* DistilGPT-2
* GPT-2 Medium

---

## 📈 Model Leaderboard

| Model        | Factual | Safety | Bias | Refusal | Final Score |
| ------------ | ------- | ------ | ---- | ------- | ----------- |
| GPT-2 Medium | 0.75    | 0.70   | 0.72 | 0.65    | 0.72        |
| GPT-2        | 0.72    | 0.65   | 0.70 | 0.60    | 0.69        |
| DistilGPT2   | 0.68    | 0.60   | 0.66 | 0.55    | 0.64        |

---

## 📊 Benchmark Visualization

* DistilGPT2   |█████████████      0.64
* GPT-2        |███████████████    0.69
* GPT-2 Medium |█████████████████  0.72

---

## ⚙️ Tech Stack

* 🐍 Python
* 🤗 Transformers (Hugging Face)
* 🧠 Sentence Transformers
* 📊 Pandas, Matplotlib
* 📚 Datasets (TruthfulQA-inspired)

---

## 🏗️ Project Structure

```bash
llm-safety-evaluation-toolkit/
│
├── notebooks/          # Experiments & analysis
├── src/                # Core evaluation pipeline
├── data/               # Dataset (raw + processed)
├── results/            # Outputs & visualizations
├── docs/               # Methodology
├── tests/              # Unit tests
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/llm-safety-evaluation-toolkit.git
cd llm-safety-evaluation-toolkit

pip install -r requirements.txt
```

Run the notebook:

```bash
notebooks/llm_safety_evaluation.ipynb
```

---

## 🔍 Key Insights

* Models perform well on factual queries but struggle with misleading prompts
* Unsafe queries are not consistently handled
* Bias exists across demographic variations
* Larger models show improved robustness

---

## 🧠 Future Work

* Integrate API-based models (GPT, Claude)
* Expand benchmark datasets
* Improve fairness and bias evaluation
* Build interactive dashboards for real-time analysis

---

## 👨‍💻 Author

**Mufid Panhalkar**
AI/ML Engineer | LLM Safety & Evaluation

---
