# Chrome Dino Game Automation

This project automates the Chrome Dino Game using Selenium and image processing libraries. The automation script allows the Dino to play the game autonomously by recognizing obstacles and jumping at the right time.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with this project, clone the repository and install the required dependencies.

```bash
git clone https://github.com/naitridoshi/Chrome-Dino-Game-Automation.git
pip install -r requirements.txt
```

## Usage

1. **Configure the script:**
   - Ensure you have the Chrome browser installed.
   - Download the appropriate ChromeDriver for your version of Chrome and ensure it is in your system PATH.

2. **Run the script:**
   - Execute the main script to start the automation.

```bash
python dino_automation.py
```

3. **Headless Mode:**
   - The script runs in headless mode (`headless=True`). You can observe the game's progress through the changing images in `bg.png` stored in the `images` directory of this repository.

4. **Output:**
   - The script will automatically open the Chrome Dino Game and start playing by itself.

## Features

- Automates the Chrome Dino Game using Selenium.
- Utilizes image processing to detect obstacles.
- Controls the Dino's jumps to avoid obstacles.
- Works with different screen resolutions.
- Runs in headless mode with real-time game images saved to `bg.png`.

## Dependencies

- Python 3.7+
- Selenium
- OpenCV
- NumPy

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

You also need to download the appropriate ChromeDriver for your version of Chrome and ensure it is in your system PATH.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or create a pull request.

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


