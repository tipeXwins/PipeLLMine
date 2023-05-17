# TFG-LMBugFixing

## VIRTUAL ENVIRONMENT OF THE PIPELINE

Si hay que instalar librerías de python para ejecutar tests o pruebas en local, ejecutar des del directorio base de proyecto:
How to initialize the virtual environment

$: python3 -m venv clmpipeline 

-- Activate the virtual environment

```$: source clmpipeline/bin/activate```

-- Upgrade pip and wheel and install dependencies

```$: pip install -U pip wheel```
```$: pip install -r requirements.txt```

-- Installl new dependencies

```$: pip3 install ...[libraries to add]...```

-- Make tests, features, etc.

-- Save new dependencies on requierements for new users

```$: pip3 freeze > requirements.txt```

-- Deactivate the environment

```$: deactivate```

## Manage saved models from HuggingFace
For deleting models from cache this dependencies should be installed: 

```pip3 install huggingface_hub\["cli"\]```
### Commands:
-- List Current Saved Models

```huggingface-cli scan-cache -v```

-- Delete Models

```huggingface-cli delete-cache```







