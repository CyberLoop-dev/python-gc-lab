<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101b2a,100:15803d&height=170&section=header&text=Python%20GC%20Lab&fontColor=ecfdf5&fontSize=42" width="100%" alt="Python GC Lab banner"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=900&color=86EFAC&center=true&vCenter=true&width=620&lines=Explore+cyclic+garbage+collection;Measure+reclaimed+reference+cycles" alt="Animated tagline"/>
<p><strong>A dependency-free CLI for a controlled Python garbage-collection experiment.</strong></p>
<img src="https://img.shields.io/github/license/CyberLoop-dev/python-gc-lab?style=flat-square" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/python-gc-lab?style=flat-square" alt="Language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/python-gc-lab?style=flat-square" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/python-gc-lab?style=flat-square" alt="Last commit"/>
<br/><img src="./assets/mark.svg" width="90%" alt="Reference cycle illustration"/>
</div>

## 🧭 Overview
Python GC Lab creates a bounded set of self-referencing Python objects, releases the references, and asks the cyclic garbage collector to reclaim them. It reports collector thresholds, counts, and reclaimed cycles.

## ✨ Features
- ♻️ Create controlled self-reference cycles.
- 📊 Report tracked objects and collected object counts.
- 🧮 Show GC generation counts and thresholds.
- 🧾 Emit readable text or JSON output.
- 🛡️ Avoid inspecting or modifying other processes.

## 🎬 Demo
Run the command to create 100 cycles and observe how many become unreachable and are reclaimed. Use the JSON option for scripting.

## 🚀 Quick Start
Requires Python 3.10 or newer. No third-party packages are needed.

```bash
python main.py
```

Use `python main.py --cycles 500 --json` for structured output, or `python main.py --no-demo` to inspect settings only. Run checks with `python -m unittest discover -s tests -v`.

## 🧰 Tech Stack
- 🐍 Python standard library: gc, weakref, argparse, json
- 🧪 unittest

## 🗂️ Folder Structure
```text
main.py                 CLI and controlled GC experiment
tests/test_gc_lab.py    Automated tests
assets/mark.svg         Original project illustration
requirements.txt        No external dependencies
.github/workflows/      Python CI
```

## 🛣️ Roadmap
- [ ] Add a generation-by-generation collection mode.
- [ ] Compare cyclic and reference-counted object lifetimes.
- [ ] Export a compact before/after report.

## 🤝 Contributing
Contributions are welcome. Keep experiments bounded and deterministic, and never make the tool modify global garbage-collector settings without an explicit option and tests.

## 📄 License
MIT. See LICENSE.

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:15803d,100:101b2a&height=100&section=footer" width="100%" alt="Animated wave footer"/></div>
