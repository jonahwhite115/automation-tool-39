# automation-tool-39

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

automation-tool-39 is a Python toolkit for automating repetitive tasks within PC games. It provides a framework for building reliable scripts that interact with game interfaces through input simulation and visual recognition.

## Features
- Pixel-perfect image matching to trigger actions based on on-screen elements
- Humanized mouse and keyboard inputs with variable timing
- YAML-based configuration for defining complex automation sequences
- Built-in debugging with automatic screenshot capture on errors

## Installation

```bash
git clone https://github.com/Developer/automation-tool-39.git
cd automation-tool-39
pip install -r requirements.txt
```

## Basic Usage

```python
from automation_tool_39 import AutomationBot

bot = AutomationBot()
bot.load_script("gather_resources.yaml")
bot.run()
```