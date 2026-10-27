
from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
import re
import dns.resolver
import dns.exception

app = Flask(__name__)
DATABASE = "mailcheck.db"


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS verification_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                status TEXT NOT NULL,
                reason TEXT NOT NULL,
                checked_at TEXT NOT NULL
            )
        """)


init_db()

EMAIL_PATTERN = (
    r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
)

# Set a reasonable timeout for DNS lookups.
resolver = dns.resolver.Resolver()
resolver.timeout = 3
resolver.lifetime = 5


def verify_email(email):
    email = email.strip()

    # Step 1: Validate the email format.
    if not re.fullmatch(EMAIL_PATTERN, email):
        return {
            "email": email,
            "status": "Likely bounce",
            "reason": "Invalid email format"
        }

    domain = email.rsplit("@", 1)[1]

    try:
        # Step 2: Check for mail exchange (MX) records.
        resolver.resolve(domain, "MX")

        return {
            "email": email,
            "status": "Likely delivered",
            "reason": (
                "Domain has mail records; "
                "mailbox is not confirmed"
            )
        }

    except dns.resolver.NXDOMAIN:
        return {
            "email": email,
            "status": "Likely bounce",
            "reason": "Domain does not exist"
        }

    except dns.resolver.NoAnswer:
        # Step 3: If MX is absent, check fallback address records.
        for record_type in ("A", "AAAA"):
            try:
                resolver.resolve(domain, record_type)

                return {
                    "email": email,
                    "status": "Unknown",
                    "reason": (
                        "No MX record; domain has an address record, "
                        "but email delivery is unconfirmed"
                    )
                }

            except dns.resolver.NXDOMAIN:
                return {
                    "email": email,
                    "status": "Likely bounce",
                    "reason": "Domain does not exist"
                }

            except dns.resolver.NoAnswer:
                continue

            except dns.exception.DNSException:
                return {
                    "email": email,
                    "status": "Unknown",
                    "reason": "DNS lookup could not be completed"
                }

        return {
            "email": email,
            "status": "Unknown",
            "reason": "No MX or usable address record found"
        }

    except dns.exception.DNSException:
        return {
            "email": email,
            "status": "Unknown",
            "reason": "DNS lookup could not be completed"
        }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/verify", methods=["POST"])

@app.route("/verify", methods=["POST"])
def verify():
    # Step 1: Validate the incoming request.
    if not request.is_json:
        return jsonify({"error": "Send data as JSON"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    emails = data.get("emails", [])

    if not isinstance(emails, list):
        return jsonify({"error": "Emails must be provided as a list"}), 400

    if len(emails) > 500:
        return jsonify({"error": "Maximum 500 emails per batch"}), 400

    # Step 2: Remove empty entries and ignore non-string values.
    emails = [
        email.strip()
        for email in emails
        if isinstance(email, str) and email.strip()
    ]

    # Step 3: Verify emails and cache duplicates.
    cache = {}
    results = []

    for email in emails:
        key = email.lower()

        if key not in cache:
            cache[key] = verify_email(email)

        results.append(cache[key].copy())

    # Step 4: Save verification results to SQLite.
    checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with sqlite3.connect(DATABASE) as conn:
        conn.executemany(
            """
            INSERT INTO verification_history
            (email, status, reason, checked_at)
            VALUES (?, ?, ?, ?)
            """,
            [
                (
                    item["email"],
                    item["status"],
                    item["reason"],
                    checked_at
                )
                for item in results
            ]
        )

    # Step 5: Return results to the frontend.
    return jsonify({"results": results})

    if len(emails) > 500:
        return jsonify({"error": "Maximum 500 emails per batch"}), 400

    # Ignore non-string and empty entries.
    emails = [
        email.strip()
        for email in emails
        if isinstance(email, str) and email.strip()
    ]

    # Step 5: Cache duplicate addresses within this batch.
    cache = {}
    results = []

    for email in emails:
        key = email.lower()

        if key not in cache:
            cache[key] = verify_email(email)

        results.append(cache[key].copy())

    return jsonify({"results": results})


@app.route("/history")
def history():
    with sqlite3.connect(DATABASE) as conn:
        conn.row_factory = sqlite3.Row

        records = conn.execute("""
            SELECT email, status, reason, checked_at
            FROM verification_history
            ORDER BY id DESC
            LIMIT 500
        """).fetchall()

    return render_template("history.html", records=records)



@app.route("/analytics")
def analytics():
    with sqlite3.connect(DATABASE) as conn:
        total = conn.execute("""
            SELECT COUNT(*) FROM verification_history
        """).fetchone()[0]

        delivered = conn.execute("""
            SELECT COUNT(*) FROM verification_history
            WHERE status = 'Likely delivered'
        """).fetchone()[0]

        bounce = conn.execute("""
            SELECT COUNT(*) FROM verification_history
            WHERE status = 'Likely bounce'
        """).fetchone()[0]

        unknown = conn.execute("""
            SELECT COUNT(*) FROM verification_history
            WHERE status = 'Unknown'
        """).fetchone()[0]

    return render_template(
        "analytics.html",
        total=total,
        delivered=delivered,
        bounce=bounce,
        unknown=unknown
    )



@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug=True)
