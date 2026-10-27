# MailCheck – Bulk Email Verification Tool

## About the Project

MailCheck is a web application developed using Python and Flask to make checking email addresses easier. It allows users to enter multiple email addresses at once and view their verification results without checking each address separately.

I built this project to apply my programming knowledge to a practical problem and gain hands-on experience with web development, DNS lookups, database management, testing, and deployment.

## 🚀 Live Demo

- **Live Application:** [Try MailCheck] https://mailcheck-8hdw.onrender.com
- **GitHub Repository:** [Explore the Source Code]

*Replace these placeholder links with your actual Render and GitHub URLs.*

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
|---|---|
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

The `app
