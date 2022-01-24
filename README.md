# Dark Souls Board Game

This is a web app to track information about your game on a UI.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/)

```bash
pip install -r requirements.txt
```

## Usage
To activate venv:
```bash
# on windows
venv\Scripts\activate.bat
# on mac
source venv/bin/activate
```
To build the frontend bundles, run:
```bash
cd src/client
npm install
npm run build
```
To start the webapp, run:
```bash
python -m src.run
```
