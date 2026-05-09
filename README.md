# ccnp-prne

This repository is for CCNP Python Programming for Network Engineers.

## Build a Python environment for practice

Use a virtual environment so your practice projects stay isolated.

### 1) Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Install/upgrade tooling

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3) Write and run simple code

Create a file named `main.py`:

```python
print("Hello, network engineer!")
```

Run it:

```bash
python main.py
```

### 4) Deactivate when done

```bash
deactivate
```
