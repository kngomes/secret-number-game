# Secret Number Game

A Python guessing game where the player tries to guess a randomly generated secret number between 1 and 100.

This project started as a simple console-based game and later evolved into a web application using Flask.

## Project Versions

### 1. Console Version
A basic terminal game built with Python.

**Features:**
- Generates a random secret number.
- Provides hints (higher or lower).
- Counts the number of attempts.
- Checks user input.
- Displays the final result.

### 2. Web Version
A browser-based version built with Python and Flask.

**Features:**
- Play the guessing game directly in the browser.
- Interactive interface using HTML and CSS.
- Game logic handled by Python and Flask.

## Technologies

- Python 3
- Flask
- HTML5
- CSS3
- Git and GitHub

## Project Structure

```text
secret-number-game/
│
├── guessing-number-web-game/
│   ├── static/
│   │   └── style.css
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   └── .gitignore
│
├── main.py
├── .gitignore
└── README.md
```

## How to Run

### Console Version

1. Clone the repository.
2. Run the following command:

```bash
python main.py
```

### Web Version

1. Navigate to the web game folder:

```bash
cd guessing-number-web-game
```

2. Install Flask:

```bash
pip install flask
```

3. Run the application:

```bash
python app.py
```

4. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Purpose

This project was created as a learning exercise to practice Python programming, understand basic web development with Flask, and explore how a simple application can evolve from a console program into a web application.
