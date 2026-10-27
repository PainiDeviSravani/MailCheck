# MailCheck – Bulk Email Verification Tool

## About the Project

MailCheck is a web application developed using Python and Flask to make checking email addresses easier. It allows users to enter multiple email addresses at once and view their verification results without checking each address separately.

I built this project to apply my programming knowledge to a practical problem and gain hands-on experience with web development, DNS lookups, database management, testing, and deployment.

## 🚀 Live Demo

- **Live Application:** https://mailcheck-8hdw.onrender.com
- **GitHub Repository:** https://github.com/PainiDeviSravani/MailCheck

## ✨ Features

- **Email Format Validation:** Checks whether an email address follows the expected format.
- **Domain DNS Checking:** Checks domain DNS records to assess whether the domain may support email delivery.
- **Bulk Verification:** Allows users to check multiple email addresses in one request.
- **Duplicate Handling:** Avoids repeating verification work for duplicate addresses within the same request.
- **Verification History:** Saves verification results in an SQLite database and displays previous records.
- **Analytics Dashboard:** Shows summary statistics for verification results.
- **User-Friendly Interface:** Includes separate pages for the main dashboard, history, analytics, settings, and project information.
- **Online Deployment:** Makes the application accessible through Render.

## 🛠️ Technologies Used

| Technology | How it is used |
| Python | Application logic |
| Flask | Building the web application |
| HTML | Structuring web pages |
| CSS | Styling the interface |
| SQLite | Storing verification history |
| dnspython | Checking domain DNS records |
| Gunicorn | Running the application in production |
| Render | Hosting and deployment |
| pytest | Running automated tests |

## ⚙️ How It Works

1. The user enters one or more email addresses into the application.
2. MailCheck checks whether each address follows the expected email format.
3. For addresses with a valid format, it checks the domain's DNS records, including MX records and fallback address records where applicable.
4. Based on the available information, the application displays a result such as **Likely delivered**, **Likely bounce**, or **Unknown**.
5. The verification results are saved in the SQLite database.
6. Users can visit the History and Analytics pages to review previous results and view summary statistics.

**Important:** MailCheck performs format and domain-level DNS checks. It cannot confirm that a specific mailbox exists or guarantee that an email will be delivered successfully.

## 📁 Project Structure

```text
MailCheck/
│
├── app.py
├── requirements.txt
├── test_app.py
├── README.md
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── analytics.html
│   ├── history.html
│   └── settings.html
│
└── static/
    └── style.css
```

The `app.py` file contains the main application logic. The `templates` folder contains the HTML pages, while `static/style.css` controls the appearance of the interface. The `requirements.txt` file lists the Python packages needed to run the project, and `test_app.py` contains the project's tests.

The `mailcheck.db` SQLite database is created when the application initializes the database.

## 💻 How to Run the Project Locally

Follow these steps to run MailCheck on your computer.

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL_HERE
```

Replace the placeholder with your actual repository URL.

### Step 2: Open the project folder

```bash
cd MailCheck
```

If your repository uses a different folder name, use that name instead.

### Step 3: Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open MailCheck

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The application should now be available on your local computer.

## 🧪 Testing

MailCheck includes a test file named `test_app.py`. You can run the tests using:

```bash
python -m pytest
```

Pytest will display the results and indicate whether the tests passed or failed.

## 🌐 Deployment

The application is deployed on **Render**, making it accessible through a public URL.

The deployment configuration uses the following commands.

**Build command**

```bash
pip install -r requirements.txt
```

**Start command**

```bash
gunicorn app:app
```

## 🔒 Limitations

- The application checks email formatting and domain DNS records but cannot confirm the existence of an individual mailbox.
- Some domains may not provide enough DNS information for a clear result.
- A successful DNS check does not guarantee email delivery.
- Verification history may be lost when the hosted application restarts or redeploys if persistent storage is not configured.

## 🎯 What I Learned

Building MailCheck gave me an opportunity to work on a complete web application rather than just individual programming exercises. Through this project, I gained practical experience in:

- Developing a web application with Python and Flask.
- Validating user input and handling web requests.
- Performing DNS lookups using Python.
- Storing and retrieving information with SQLite.
- Organizing HTML templates, CSS, and application code.
- Writing and running tests with pytest.
- Deploying a Python application using Render.

## 🔮 Future Improvements

I would like to continue improving MailCheck by exploring the following features:

- Adding an option to export verification results as CSV files.
- Improving error messages and user feedback.
- Expanding automated test coverage.
- Making the analytics dashboard more informative.
- Configuring persistent storage for verification history.
- Improving performance when handling larger batches of email addresses.

## 👩‍💻 About Me

**Paini Devi Sravani**  
B.Tech – Computer Science and Engineering

I am interested in software development and enjoy learning new technologies by building practical projects. MailCheck is one of my efforts to strengthen my programming skills and gain experience in developing and deploying web applications.

---

*MailCheck is an educational project. Its verification results are indicative only and should not be treated as a guarantee of email deliverability.*
