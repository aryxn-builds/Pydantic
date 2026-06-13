<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=30&pause=1000&color=E92063&center=true&vCenter=true&width=700&lines=Pydantic+%F0%9F%94%A5;Data+Validation+in+Python;Typed.+Validated.+Bulletproof." alt="Typing SVG" />

<br/>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pydantic](https://img.shields.io/badge/Pydantic-v2-E92063?style=for-the-badge&logo=pydantic&logoColor=white)](https://docs.pydantic.dev)
[![Course](https://img.shields.io/badge/Course-CampusX-FF6B35?style=for-the-badge&logo=youtube&logoColor=white)](https://youtu.be/lRArylZCeOs)
[![Status](https://img.shields.io/badge/Status-Active-00FF88?style=for-the-badge)](#)

<br/>

> **"Bad data in, bad results out. Pydantic fixes that."**
> 
> A complete, hands-on code reference from the **CampusX Pydantic Crash Course** —
> every concept coded, tested, and documented for real-world use.

---

</div>

## ⚡ What is Pydantic?

**Pydantic** is the most widely used data validation library in Python. It uses Python type hints to validate data at runtime, serialize models to JSON, and catch bugs before they reach production — used under the hood by **FastAPI, LangChain, and hundreds of libraries**.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

user = User(name="Aryan", age=21, email="ay6033756@gmail.com")
# ✅ Validated. Typed. Production-ready.
```

---

## 📂 Repo Structure

```
pydantic-crash-course/
│
├── 01_basemodel_basics.py          # BaseModel, fields, instantiation
├── 02_field_types.py               # str, int, float, bool, List, Dict, etc.
├── 03_field_validators.py          # @field_validator, @model_validator
├── 04_default_and_optional.py      # Optional fields, default values, aliases
├── 05_nested_models.py             # Models inside models
├── 06_custom_validators.py         # Custom logic with @validator
├── 07_model_config.py              # ConfigDict, strict mode, frozen models
├── 08_serialization.py             # .model_dump(), .model_dump_json()
├── 09_json_schema.py               # .model_json_schema() for API docs
├── 10_real_world_example.py        # Full use case (API response validation)
│
└── README.md
```

---

## 🧠 Concepts Covered

| # | Topic | Key Feature |
|---|-------|-------------|
| 01 | BaseModel Basics | Define structured data models |
| 02 | Field Types | Full Python type hint support |
| 03 | Field Validators | `@field_validator`, `@model_validator` |
| 04 | Optional & Defaults | `Optional[T]`, `Field(default=...)` |
| 05 | Nested Models | Compose models within models |
| 06 | Custom Validators | Write any custom validation logic |
| 07 | Model Config | Strict mode, frozen, alias generation |
| 08 | Serialization | Export to `dict`, `JSON` |
| 09 | JSON Schema | Auto-generate OpenAPI-compatible schemas |
| 10 | Real World Example | Validate API responses end-to-end |

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/aryxn-builds/Pydantic.git
cd pydantic
```

**2. Install Pydantic**
```bash
pip install pydantic
```

**3. Run any script**
```bash
python 1.type_validation.py
```

---

## 🎯 Why This Matters for AI/ML Engineers

Pydantic is **everywhere** in the modern AI/ML stack:

- 🔗 **LangChain** — structured LLM outputs using Pydantic models
- ⚡ **FastAPI** — request/response validation out of the box
- 🤖 **OpenAI / Anthropic SDKs** — API response parsing
- 🛠️ **MLflow, Ray, Airflow** — config and pipeline validation

If you're building AI products, **Pydantic is not optional**.

---

## 📚 Course Reference

This repo follows the [**Pydantic Crash Course by CampusX**](https://youtu.be/lRArylZCeOs) — one of the best Hindi/English resources for learning data validation in Python from scratch.

---

## 🙋‍♂️ Author

<div align="center">

**Aryan Yadav** — ML/AI Engineer

[![GitHub](https://img.shields.io/badge/GitHub-aryxn--builds-181717?style=for-the-badge&logo=github)](https://github.com/aryxn-builds)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com)

*Building in public. One validated model at a time.* 🔥

</div>

---

<div align="center">

⭐ **Star this repo if it helped you** — it keeps me building in public!

</div>