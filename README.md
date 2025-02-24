# CGV IMAX Reservation Alert Bot

This project monitors the CGV movie theater website in real time to detect when IMAX reservations become available for a specific movie (e.g., **Avatar: The Way of Water**). When detected, the bot sends an immediate alert via Telegram with a direct reservation link.

## Features

- **Real-time Web Crawling:**  
  Utilizes Selenium and BeautifulSoup to periodically check the designated CGV theater page.

- **IMAX Reservation Detection:**  
  Parses the webpage to identify IMAX screening information and verifies if the movie is "Avatar: The Way of Water," triggering an alert if the reservation opens.

- **Telegram Alerts:**  
  Sends an alert message with the reservation link through a Telegram bot as soon as reservations are available.

- **Real-time Control Commands:**  
  Users can control the system via Telegram commands:
  - "정지" (Stop): Pauses the alert system.
  - "재개" (Resume): Resumes the alert system.

- **Scheduled Monitoring:**  
  Uses APScheduler to run the monitoring function every 10 seconds for prompt detection.

## Usage

1. **Install Required Libraries**  
   Install the necessary Python libraries:
   ```bash
   pip install python-telegram-bot selenium bs4 apscheduler
   ```

2. **Configuration**  
   - Set your Telegram bot token and chat ID in the script's `token` and `id` variables.
   - Ensure that you have the appropriate ChromeDriver installed and that it is compatible with your version of Chrome.
   - Adjust variables such as the target date (`date`) and the reservation URL (`mobile_url`) as needed.

3. **Execution**  
   Run the script to start the APScheduler, which will check the CGV website every 10 seconds. When the reservation for "Avatar: The Way of Water" is detected, the bot sends an alert message via Telegram.

4. **Control Commands**  
   - Sending "정지" via Telegram will pause the alert system.
   - Sending "재개" will resume the system.

## Code Overview

- **`job_function()`**  
  Opens the CGV theater page using Selenium, switches to the iframe containing the movie times, and parses the page with BeautifulSoup. It checks for the presence of an IMAX screening for "Avatar: The Way of Water" and sends a Telegram alert if detected.

- **`handler()`**  
  A message handler that listens for user commands ("정지" or "재개") to control the scheduler's operation.

- **APScheduler (BlockingScheduler):**  
  Executes the `job_function()` at 10-second intervals to ensure continuous monitoring.

## Notes

- **Sensitive Information:**  
  Keep your Telegram bot token and chat ID secure.

- **Website Structure Changes:**  
  If the structure of the CGV website changes, you may need to update the BeautifulSoup selectors accordingly.

- **WebDriver Compatibility:**  
  Verify that your installed ChromeDriver is compatible with your current Chrome browser version.
