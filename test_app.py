
import app as mailcheck


def test_home_page():
    client = mailcheck.app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"MailCheck" in response.data


def test_invalid_email_format():
    result = mailcheck.verify_email("invalid-email")

    assert result["status"] == "Likely bounce"
    assert result["reason"] == "Invalid email format"


def test_empty_email():
    result = mailcheck.verify_email("")

    assert result["status"] == "Likely bounce"


def test_invalid_request_format():
    client = mailcheck.app.test_client()

    response = client.post(
        "/verify",
        data="not json",
        content_type="text/plain"
    )

    assert response.status_code == 400


def test_more_than_500_emails():
    client = mailcheck.app.test_client()

    response = client.post(
        "/verify",
        json={"emails": ["test@example.com"] * 501}
    )

    assert response.status_code == 400
