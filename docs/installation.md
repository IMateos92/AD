# Guía de instalación

## Requisitos previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/IMateos92/AD.git
cd AD
```

### 2. Crear un entorno virtual (recomendado)

```bash
python -m venv venv

# En Windows
venv\Scripts\activate

# En macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Instalar la aplicación en modo desarrollo

```bash
pip install -e .
```

## Verificar instalación

```bash
python -c "import src; print('¡Instalación exitosa!')"
```

## Próximos pasos

Consulta la [guía de uso](usage.md) para comenzar a usar la aplicación.
