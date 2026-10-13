import streamlit as st
import string

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐"
)

st.title("🔐 Password Strength Checker")
st.write("Enter a password to analyze its strength.")

password = st.text_input(
    "Enter your password",
    type="password",
    help="Your password is hidden while typing."
)

if password:
    # Check password criteria
    length_ok = len(password) >= 8
    uppercase_ok = any(c.isupper() for c in password)
    lowercase_ok = any(c.islower() for c in password)
    number_ok = any(c.isdigit() for c in password)
    special_ok = any(c in string.punctuation for c in password)

    criteria = {
        "At least 8 characters": length_ok,
        "Contains an uppercase letter": uppercase_ok,
        "Contains a lowercase letter": lowercase_ok,
        "Contains a number": number_ok,
        "Contains a special character": special_ok
    }

    # Calculate strength
    score = sum(criteria.values())

    st.subheader("Password Strength Analysis")
    st.write(f"Criteria satisfied: {score}/5")

    for criterion, passed in criteria.items():
        if passed:
            st.success(f"✓ {criterion}")
        else:
            st.error(f"✗ {criterion}")

    # Classify password strength
    if score <= 2:
        strength = "Weak"
        st.error(f"Password Strength: {strength}")
    elif score <= 4:
        strength = "Moderate"
        st.warning(f"Password Strength: {strength}")
    else:
        strength = "Strong"
        st.success(f"Password Strength: {strength}")

    # Suggestions
    suggestions = [
        message for passed, message in [
            (length_ok, "Use at least 8 characters."),
            (uppercase_ok, "Add an uppercase letter (A-Z)."),
            (lowercase_ok, "Add a lowercase letter (a-z)."),
            (number_ok, "Include a number (0-9)."),
            (special_ok, "Include a special character (!, @, #, etc.).")
        ] if not passed
    ]

    if suggestions:
        st.subheader("Suggestions for Improvement")
        for suggestion in suggestions:
            st.write(f"• {suggestion}")
    else:
        st.info("All criteria satisfied! Use a unique password "
                "and consider making it longer.")
