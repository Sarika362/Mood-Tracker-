
# Mood Tracker 😃

## Overview

Mood Tracker is a simple web application built with Flask to help users log and monitor their mood over time. 🌟 The application allows users to record their mood, add optional comments, view a summary of mood entries, and clear previous logs. It uses an in-memory list to store mood entries and provides a straightforward interface to track emotional well-being. 💭

## Features

- **Mood Logging**: Log your mood with options such as Happy 😃, Sad 😢, Angry 😠, Anxious 😰, and Excited 😆.
- **Comments**: Add optional comments to each mood entry. 💬
- **Mood Summary**: View a summary of how many times each mood has been logged. 📊
- **Clear Moods**: Clear all mood entries from the log. ❌

## Technologies Used

- **Backend**: Flask (Python) 🐍
- **Frontend**: HTML, Bootstrap 4 🎨
- **Database**: In-memory list (for simplicity) 🗂️

## Installation

### Clone the Repository

```bash
git clone https://github.com/Sarika362/Mood-Tracker-.git
cd Mood-Tracker-
```

### Set Up the Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Ensure that `requirements.txt` includes Flask. If it’s not there, you can create it by running:

```bash
pip freeze > requirements.txt
```

## Running the Application

To start the Flask development server:

```bash
flask run
```

By default, the application will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/). 🌐

## Usage

1. **Log Mood**: Access the application and select your mood from the dropdown. Optionally, add a comment and click "Log Mood." 📝
2. **View Mood Log**: See your mood entries listed below the logging form. 📜
3. **View Mood Summary**: Click the "View Mood Summary" button to see a summary of mood counts. 📈
4. **Clear Moods**: Click the "Clear Moods" button to remove all entries from the log. 🗑️

## Project Structure

- `main.py`: The main Flask application file. 🗃️
- `src/index.html`: The main interface for logging and viewing moods. 📄
- `src/mood_summary.html`: The page for viewing mood summary. 📄

## Contributing

1. Fork the repository. 🍴
2. Create a new branch (`git checkout -b feature-branch`). 🌿
3. Commit your changes (`git commit -am 'Add new feature'`). 📝
4. Push to the branch (`git push origin feature-branch`). 🚀
5. Create a new Pull Request. 🔄

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 📜

## Contact

For any questions or feedback, please contact:

- **Name**: Sarika M N 🌟
- **Email**: [sarika.mn97@gmail.com](mailto:sarika.mn97@gmail.com)
- **GitHub**: [Sarika362](https://github.com/Sarika362) 🐙

## Acknowledgements

- Flask documentation and community for support. 🙏
- Bootstrap for the styling framework. 🎨
