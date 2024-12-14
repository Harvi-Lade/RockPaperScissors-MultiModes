# RockPaperScissors-MultiModes

RockPaperScissors-MultiModes is a dynamic and engaging Python-based implementation of the classic Rock, Paper, Scissors game. This project takes the timeless game to the next level with three unique gameplay modes, built-in statistics tracking, and a sleek, user-friendly experience. Whether you're playing solo, competing with friends, or racing against the clock, this project delivers hours of entertainment!


---


### 🎮 Features

1. **Single-Player Mode:**

Challenge yourself against a computer opponent. Test your skills and strategy while the computer makes random choices.
  Real-time gameplay: Get instant results for each round.
  Fair competition: The computer opponent uses unbiased random selection.

2. **Multiplayer Mode:**

Bring your friends into the fun! Two players can face off to determine the ultimate Rock, Paper, Scissors champion.
  Hidden Input: Choices remain secret until both players have locked them in.
  Interactive fun: Perfect for friendly competitions or family game nights.

3. **Timed Mode:**

Race against the clock! Test how many rounds you can complete within a set time limit.
  Customizable time settings: Set your own limits (e.g., 30, 60 seconds).
  Score tracking: See how well you perform under pressure.

4. **Statistics Tracking:**

Keep a record of your games to analyze and celebrate your achievements!
  Win/Loss/Draw stats: Track your performance over time.
  JSON file storage: View or reset your game history anytime.


---


### 🔍 Modules Used

This project leverages the power of Python's built-in libraries to deliver a seamless gaming experience:
  ```
  random: For generating random choices for the computer opponent.
  ```

  ```
  time: To track and manage the timed mode gameplay.
  ```
  
  ```
  json: For saving and retrieving game statistics in a structured format.
  ```

  ```
  logging: To maintain logs for debugging and tracking application behavior.
  ```
  ```
  getpass: To hide player input during multiplayer mode.
  ```
  ```
  re: For validating player names and ensuring input accuracy.
  ```
  ```
  datetime: To timestamp game statistics.
  ```

No additional third-party modules are required, making setup quick and simple!


---


### 🚀 Installation

Follow these steps to set up and run the project on your local system:

### Prerequisites
- Python 3.10 or later
- Git (to clone the repository)

### Steps

1. **Clone the Repository**  

   Open your terminal and run the following command:

   https://github.com/Harvi-Lade/RockPaperScissors-MultiModes

3. **Run the Game**

  python rock_paper_scissors_multimodes.py


---


### 📋 How to Play

Launch the game and choose from these modes:
  
  1. Single Player Mode
  
  2. Multiplayer Mode
  
  3. Timed Mode
  
  4. View Statistics

Follow the on-screen prompts to input player names, set rounds/times, and make your choices.

Play and enjoy!

View your performance stats at any time using the View Statistics option.


---


### 🔧 Customization

Want to tweak the game? Here’s how:
  
  1. Change Max Statistics Entries:

     Update the MAX_ENTRIES variable in the code to control how many game records are saved.
  
  2. Modify Emoji Icons:

     Edit the CHOICES dictionary to customize how Rock, Paper, and Scissors are represented.


---


### 💾 How Stats are Saved

Statistics are saved in a game_statistics.json file. This file stores details like:
 
  - Player names
  
  - Wins, losses, and draws
  
  - Number of rounds played
  
  - Timestamps

You can reset the stats by deleting the file or modifying its contents directly.


---


### 🌟 Why Choose RockPaperScissors-MultiModes?
  
  - Fun for Everyone: Play solo or with friends and family.
  
  - Customizable Gameplay: Tailor modes and settings to your preference.
  
  - Track Your Progress: Save and revisit your performance over time.
  
  - Easy Setup: Run it anywhere Python is installed.


---


### 🛠️ **Skills and Technologies Used**  

- **Programming Language:**  
  - Python  

- **Object-Oriented Design (OOP):**  
  - Implemented a class-based architecture to ensure modularity, reusability, and adherence to **DRY (Don't Repeat Yourself)** principles.  

- **Game Mechanics Development:**  
  - Designed and developed a fully functional **Rock-Paper-Scissors** game with multiple interactive modes (Single Player, Multiplayer, and Timed Mode).  

- **Data Management and Persistence:**  
  - Utilized JSON to manage game statistics with seamless saving and loading capabilities.  

- **Input Validation and Error Handling:**  
  - Built robust input validation mechanisms to enhance user experience and prevent invalid inputs.  

- **Command Line Interface (CLI):**  
  - Delivered a dynamic and user-friendly terminal-based game experience.  

- **Logging and Debugging:**  
  - Leveraged Python's `logging` module to monitor key gameplay events and debug efficiently.  

- **Randomization and AI Logic:**  
  - Integrated the `random` module to create computer AI for the game, ensuring unpredictability in the opponent's choices.  

- **Time-Based Features:**  
  - Used Python's `time` module for implementing a timed game mode with countdown functionality.  

- **Code Refactoring and Optimization:**  
  - Transitioned from function-based programming to class-based programming, improving scalability, modularity, and readability.  

- **Adherence to Best Practices:**  
  - Followed **clean code** principles and implemented **modular design** to enhance maintainability.  

- **Version Control and Collaboration:**  
  - Managed project iterations using **Git** and hosted the project on **GitHub** for collaboration.  

- **Documentation:**  
  - Provided comprehensive project documentation using Markdown for clear and concise communication.  


---


### 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.
  
  1. Fork the project.
  
  2. Create your feature branch: git checkout -b feature/NewFeature.
  
  3. Commit your changes: git commit -m 'Add a NewFeature'.
  
  4. Push to the branch: git push origin feature/NewFeature.
  
  5. Open a pull request.


---


### 🤝 Connect with Me

If you enjoyed this project or have feedback, feel free to connect with me:

Name: Harvi Lade

- LinkedIn: https://www.linkedin.com/in/harvilade2102/

- GitHub: https://github.com/Harvi-Lade


---


Feel free to reach out if you have questions, suggestions, or feedback!
