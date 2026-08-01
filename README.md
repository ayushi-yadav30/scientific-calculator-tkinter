# Scientific Calculator 🧮

A modern scientific calculator built with Python and CustomTkinter, featuring trigonometric, logarithmic, and power functions with a clean, intuitive GUI.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 About the Project

This is a Scientific Calculator built using Python, designed to handle both basic arithmetic and advanced scientific operations through a clean, modern graphical interface.

The project started as a basic calculator supporting core operations (addition, subtraction, multiplication, division) and was progressively upgraded to include scientific functions like trigonometry (sin, cos, tan), logarithms, powers, roots, and factorials — with support for both Degree and Radian modes.

This project was built as part of my learning journey in Python and GUI development, with a focus on writing clean, modular, and well-structured code.

---

## ✨ Features

- Basic arithmetic operations (+, −, ×, ÷)
- Scientific functions: sin, cos, tan, log, ln, √, x², xʸ, n!
- DEG / RAD mode toggle for trigonometric calculations
- Constants: π and e
- Error handling for invalid inputs (e.g., divide by zero, math domain errors)
- Clean and responsive GUI built with CustomTkinter

---

## 🖼️ Screenshots

| Basic Mode | Scientific Mode |
|:----------:|:----------------:|
| _screenshot coming soon_ | _screenshot coming soon_ |



---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **GUI Library:** CustomTkinter
- **Core Module:** math (for scientific calculations)

---

## 📂 Project Structure

```
scientific-calculator/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── main.py              # Entry point - app runs from here
│   ├── calculator_logic.py  # Calculation logic (backend)
│   ├── ui.py                # GUI layout and buttons
│   └── utils.py             # Helper functions
│
├── assets/
│   └── icon.png
│
├── screenshots/
│   ├── basic_mode.png
│   └── scientific_mode.png
│
└── tests/
    └── test_calculator.py
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/ayushi-yadav-30 /scientific-calculator.git
   cd scientific-calculator
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application
   ```bash
   python src/main.py
   ```

---

## 🎯 Usage

- Use the number pad and operator buttons for basic calculations.
- Toggle between **DEG** and **RAD** mode before using trigonometric functions.
- Use scientific function buttons (sin, cos, tan, log, √, etc.) for advanced calculations.
- Press **C** to clear the display and start a new calculation.

---

## 🔮 Future Improvements

- [ ] Add calculation history panel
- [ ] Add keyboard input support
- [ ] Add dark/light theme toggle
- [ ] Add memory functions (M+, M−, MR, MC)
- [ ] Package as a standalone executable

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](../../issues) if you'd like to contribute.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👩‍💻 Author

**Ayushi**
Built as part of my Python and GUI development learning journey.
