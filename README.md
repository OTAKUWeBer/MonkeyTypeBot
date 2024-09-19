# MonkeyTypeBot

This script automates typing tests on Monkeytype.com using Selenium WebDriver. You can log in with your email and password or start typing without logging in. The script allows you to control typing speed and page mode.

## Features

- **Login with Email and Password**: Automate typing tests while logged in.
- **Start Without Login**: Directly start typing tests without authentication.
- **Customizable Typing Speed**: Set the time interval between typing each character.
- **Mode Switching**: Specify the time to switch between typing modes.

## Requirements

- Python 3.x
- Selenium WebDriver
- [Geckodriver](https://github.com/mozilla/geckodriver/releases) (for Firefox) or [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/) (for Chrome)

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/OTAKUWeBer/MonkeyTypeBot.git
   cd MonkeyTypeBot
   ```

2. **Install Dependencies**:

   Install the necessary Python package:

   ```bash
   pip install selenium
   ```

3. **Download WebDriver**:

   - **For Firefox**: Download `geckodriver` from [here](https://github.com/mozilla/geckodriver/releases) and place it in your desired location.
   - **For Chrome**: Download `chromedriver` from [here](https://googlechromelabs.github.io/chrome-for-testing/) and place it in your desired location.

4. **Update the Script**:

   Edit the script to specify the path to your WebDriver executable and select your browser. Update the following variables in `main.py`:

   ```python
   # Specify the browser to use: "Firefox" or "Chrome"
   browser = "Firefox"

   # Path to the WebDriver executable
   # For Firefox, this should be the path to geckodriver
   # For Chrome, this should be the path to chromedriver
   path = "/path/to/your/webdriver"  # Update this with the actual path
   ```

## Usage

Run the script and follow the prompts:

```bash
python main.py
```

You will be prompted to choose between logging in or starting without login, and to enter typing speed and mode-switching time.

### Login Method

1. **Enter Email and Password**: Provides a login option.
2. **Enter Typing Speed**: Time between typing each character (e.g., 0.1 for ~100 WPM).
3. **Enter Mode Switching Time**: Seconds to wait before switching mode (0 for no switch).

### Without Login

1. **Enter Typing Speed**: Time between typing each character (e.g., 0.1 for ~100 WPM).
2. **Enter Mode Switching Time**: Seconds to wait before switching mode (0 for no switch).

## Troubleshooting

- Ensure that the path to your WebDriver executable is correctly set.
- Make sure the WebDriver version matches your browser version.
- If encountering issues with the script, check the console output for error messages.