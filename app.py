import streamlit as st

st.title('Movie Ticket Booking System')
st.markdown('---')
st.text_input('Enter your name:')
st.text_input('Enter your email:')
st.number_input('Enter your mobile number:')
st.text_input('Enter your city:')
st.selectbox('Select Movie:',options = ['Hum aapke hain kon','Maine pyar kiya','Hum saath saath hai'])
st.date_input('select Date')
st.radio('Select slot',options = ['9am-12pm','12pm-3pm','3pm-6pm','6pm-9pm'])
st.number_input('Enter number of seats:')
st.multiselect('Select Meal:',options = ['Popcorn','Burger','French fries','Pizza','Chocolate lava cake'])
st.selectbox('Payment Method:',options = ['UPI','Credit/Debit card','Net banking'])
st.button('Done')

import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #f5f7fa;
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        color: #1f2937;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 25px;
    }

    /* Form container */
    [data-testid="stForm"] {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.10);
        border: 1px solid #e5e7eb;
    }

    /* Section headings */
    .section-title {
        font-size: 20px;
        font-weight: bold;
        color: #374151;
        margin-top: 10px;
        margin-bottom: 10px;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 45px;
        border-radius: 8px;
        font-size: 17px;
        font-weight: bold;
    }

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🎬 Movie Ticket Booking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your movie tickets quickly and easily</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# ---------------- BOOKING FORM ----------------
with st.form("movie_booking_form"):

    st.markdown(
        '<div class="section-title">👤 Customer Details</div>',
        unsafe_allow_html=True
    )

    # First row
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Enter your name:",
            placeholder="Enter full name"
        )

    with col2:
        email = st.text_input(
            "Enter your email:",
            placeholder="example@gmail.com"
        )

    # Second row
    col1, col2 = st.columns(2)

    with col1:
        mobile = st.text_input(
            "Enter mobile number:",
            placeholder="Enter 10 digit mobile number"
        )

    with col2:
        city = st.text_input(
            "Enter your city:",
            placeholder="Enter city"
        )

    st.markdown("---")

    # ---------------- MOVIE DETAILS ----------------
    st.markdown(
        '<div class="section-title">🎥 Movie Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        movie = st.selectbox(
            "Select Movie:",
            options=[
                "Hum Aapke Hain Koun",
                "Maine Pyar Kiya",
                "Hum Saath Saath Hain"
            ]
        )

    with col2:
        booking_date = st.date_input(
            "Select Date:"
        )

    # Slot and seats
    col1, col2 = st.columns(2)

    with col1:
        slot = st.radio(
            "Select Slot:",
            options=[
                "9 AM - 12 PM",
                "12 PM - 3 PM",
                "3 PM - 6 PM",
                "6 PM - 9 PM"
            ]
        )

    with col2:
        seats = st.number_input(
            "Number of Seats:",
            min_value=1,
            max_value=10,
            value=1,
            step=1
        )

    st.markdown("---")

    # ---------------- FOOD & PAYMENT ----------------
    st.markdown(
        '<div class="section-title">🍿 Food & Payment</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        meals = st.multiselect(
            "Select Meal:",
            options=[
                "Popcorn",
                "Burger",
                "French Fries",
                "Pizza",
                "Chocolate Lava Cake"
            ]
        )

    with col2:
        payment_method = st.selectbox(
            "Payment Method:",
            options=[
                "UPI",
                "Credit/Debit Card",
                "Net Banking"
            ]
        )

    st.markdown("---")

    # ---------------- SUBMIT ----------------
    submitted = st.form_submit_button(
        "🎟️ Confirm Booking"
    )


# ---------------- AFTER SUBMISSION ----------------
if submitted:

    if name == "" or email == "" or mobile == "" or city == "":
        st.error("⚠️ Please fill in all customer details.")

    elif len(mobile) != 10 or not mobile.isdigit():
        st.error("⚠️ Please enter a valid 10-digit mobile number.")

    else:
        st.success("✅ Booking details submitted successfully!")

        st.markdown("### 🎫 Booking Summary")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Customer Name:**", name)
            st.write("**Email:**", email)
            st.write("**Mobile:**", mobile)
            st.write("**City:**", city)

        with col2:
            st.write("**Movie:**", movie)
            st.write("**Date:**", booking_date)
            st.write("**Slot:**", slot)
            st.write("**Seats:**", seats)

        st.write("**Meals:**", ", ".join(meals) if meals else "No meal selected")
        st.write("**Payment Method:**", payment_method)

        import streamlit as st
import sqlite3
from datetime import date


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Movie Ticket Booking",
    page_icon="🎬",
    layout="wide"
)


# =========================================================
# DATABASE CONNECTION
# =========================================================

def get_connection():
    return sqlite3.connect("movie_booking.db")


# =========================================================
# CREATE DATABASE TABLE
# =========================================================

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            email TEXT NOT NULL,
            mobile TEXT NOT NULL,
            city TEXT NOT NULL,
            movie TEXT NOT NULL,
            booking_date TEXT NOT NULL,
            slot TEXT NOT NULL,
            seats INTEGER NOT NULL,
            meals TEXT,
            payment_method TEXT NOT NULL,
            ticket_fare REAL NOT NULL,
            meal_fare REAL NOT NULL,
            total_fare REAL NOT NULL,
            booking_status TEXT DEFAULT 'Confirmed'
        )
    """)

    conn.commit()
    conn.close()


create_table()


# =========================================================
# FARE DETAILS
# =========================================================

movie_fares = {
    "Hum Aapke Hain Koun": 180,
    "Maine Pyar Kiya": 150,
    "Hum Saath Saath Hain": 160
}

meal_fares = {
    "Popcorn": 120,
    "Burger": 150,
    "French Fries": 100,
    "Pizza": 200,
    "Chocolate Lava Cake": 180
}


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fa;
}

.main-title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #1f2937;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 17px;
    margin-bottom: 25px;
}

.section-title {
    font-size: 22px;
    font-weight: bold;
    color: #374151;
    margin-top: 10px;
    margin-bottom: 15px;
}

[data-testid="stForm"] {
    background-color: white;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-weight: bold;
}

.booking-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #ddd;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎬 Movie Ticket Booking System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Book your movie tickets quickly and easily</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🎬 Movie Booking")

menu = st.sidebar.radio(
    "Select Option",
    [
        "🎟️ New Booking",
        "🔎 Search Booking",
        "📋 View All Bookings",
        "❌ Cancel Booking"
    ]
)


# =========================================================
# NEW BOOKING
# =========================================================

if menu == "🎟️ New Booking":

    st.markdown(
        '<div class="section-title">🎟️ Enter Booking Details</div>',
        unsafe_allow_html=True
    )

    with st.form("booking_form"):

        # -------------------------------------------------
        # CUSTOMER DETAILS
        # -------------------------------------------------

        st.subheader("👤 Customer Details")

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Customer Name",
                placeholder="Enter full name"
            )

            email = st.text_input(
                "Email",
                placeholder="example@gmail.com"
            )

        with col2:

            mobile = st.text_input(
                "Mobile Number",
                placeholder="10 digit mobile number"
            )

            city = st.text_input(
                "City",
                placeholder="Enter city"
            )

        st.markdown("---")

        # -------------------------------------------------
        # MOVIE DETAILS
        # -------------------------------------------------

        st.subheader("🎥 Movie Details")

        col1, col2 = st.columns(2)

        with col1:

            movie = st.selectbox(
                "Select Movie",
                list(movie_fares.keys())
            )

            booking_date = st.date_input(
                "Select Date",
                min_value=date.today()
            )

        with col2:

            slot = st.selectbox(
                "Select Slot",
                [
                    "9 AM - 12 PM",
                    "12 PM - 3 PM",
                    "3 PM - 6 PM",
                    "6 PM - 9 PM"
                ]
            )

            seats = st.number_input(
                "Number of Seats",
                min_value=1,
                max_value=10,
                value=1,
                step=1
            )

        st.markdown("---")

        # -------------------------------------------------
        # MEALS
        # -------------------------------------------------

        st.subheader("🍿 Food Selection")

        meals = st.multiselect(
            "Select Meals",
            list(meal_fares.keys())
        )

        st.markdown("---")

        # -------------------------------------------------
        # PAYMENT
        # -------------------------------------------------

        st.subheader("💳 Payment")

        payment_method = st.selectbox(
            "Payment Method",
            [
                "UPI",
                "Credit/Debit Card",
                "Net Banking"
            ]
        )

        st.markdown("---")

        submitted = st.form_submit_button(
            "🎟️ Confirm Booking"
        )


    # =====================================================
    # AFTER SUBMIT
    # =====================================================

    if submitted:

        # -------------------------------------------------
        # VALIDATION
        # -------------------------------------------------

        if name.strip() == "":
            st.error("Please enter customer name.")

        elif email.strip() == "":
            st.error("Please enter email.")

        elif mobile.strip() == "":
            st.error("Please enter mobile number.")

        elif not mobile.isdigit() or len(mobile) != 10:
            st.error("Please enter a valid 10-digit mobile number.")

        elif city.strip() == "":
            st.error("Please enter city.")

        else:

            # -------------------------------------------------
            # CALCULATE FARE
            # -------------------------------------------------

            ticket_price = movie_fares[movie]

            ticket_fare = ticket_price * seats

            meal_fare = sum(
                meal_fares[meal]
                for meal in meals
            )

            total_fare = ticket_fare + meal_fare

            meal_string = ", ".join(meals) if meals else "No Meal"


            # -------------------------------------------------
            # STORE DATA IN SQLITE
            # -------------------------------------------------

            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO bookings (
                    customer_name,
                    email,
                    mobile,
                    city,
                    movie,
                    booking_date,
                    slot,
                    seats,
                    meals,
                    payment_method,
                    ticket_fare,
                    meal_fare,
                    total_fare,
                    booking_status
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name,
                email,
                mobile,
                city,
                movie,
                str(booking_date),
                slot,
                seats,
                meal_string,
                payment_method,
                ticket_fare,
                meal_fare,
                total_fare,
                "Confirmed"
            ))

            conn.commit()

            booking_id = cursor.lastrowid

            conn.close()


            # -------------------------------------------------
            # SUCCESS MESSAGE
            # -------------------------------------------------

            st.success(
                f"🎉 Booking Confirmed! Your Booking ID is #{booking_id}"
            )

            # -------------------------------------------------
            # BOOKING SUMMARY
            # -------------------------------------------------

            st.subheader("🎫 Booking Summary")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write("**Booking ID:**", booking_id)
                st.write("**Customer:**", name)
                st.write("**Email:**", email)
                st.write("**Mobile:**", mobile)

            with col2:

                st.write("**Movie:**", movie)
                st.write("**Date:**", booking_date)
                st.write("**Slot:**", slot)
                st.write("**Seats:**", seats)

            with col3:

                st.write("**Ticket Fare:** ₹", ticket_fare)
                st.write("**Meal Fare:** ₹", meal_fare)
                st.write("**Total Fare:** ₹", total_fare)
                st.write("**Payment:**", payment_method)

            st.info(
                f"🍿 Meals: {meal_string}"
            )


# =========================================================
# SEARCH BOOKING
# =========================================================

elif menu == "🔎 Search Booking":

    st.subheader("🔎 Search Booking")

    booking_id = st.number_input(
        "Enter Booking ID",
        min_value=1,
        step=1
    )

    if st.button("🔍 Search"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM bookings
            WHERE booking_id = ?
        """, (booking_id,))

        booking = cursor.fetchone()

        conn.close()

        if booking:

            st.success("Booking Found!")

            st.write("### 🎫 Booking Details")

            col1, col2 = st.columns(2)

            with col1:

                st.write("**Booking ID:**", booking[0])
                st.write("**Customer Name:**", booking[1])
                st.write("**Email:**", booking[2])
                st.write("**Mobile:**", booking[3])
                st.write("**City:**", booking[4])
                st.write("**Movie:**", booking[5])
                st.write("**Booking Date:**", booking[6])

            with col2:

                st.write("**Slot:**", booking[7])
                st.write("**Seats:**", booking[8])
                st.write("**Meals:**", booking[9])
                st.write("**Payment:**", booking[10])
                st.write("**Ticket Fare:** ₹", booking[11])
                st.write("**Meal Fare:** ₹", booking[12])
                st.write("**Total Fare:** ₹", booking[13])
                st.write("**Status:**", booking[14])

        else:

            st.error("❌ Booking not found.")


# =========================================================
# VIEW ALL BOOKINGS
# =========================================================

elif menu == "📋 View All Bookings":

    st.subheader("📋 All Bookings")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            booking_id,
            customer_name,
            movie,
            booking_date,
            slot,
            seats,
            total_fare,
            booking_status
        FROM bookings
        ORDER BY booking_id DESC
    """)

    bookings = cursor.fetchall()

    conn.close()


    if bookings:

        for booking in bookings:

            st.markdown(
                '<div class="booking-card">',
                unsafe_allow_html=True
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.write(
                    f"### 🎫 Booking #{booking[0]}"
                )

                st.write(
                    f"**Customer:** {booking[1]}"
                )

                st.write(
                    f"**Movie:** {booking[2]}"
                )

            with col2:

                st.write(
                    f"**Date:** {booking[3]}"
                )

                st.write(
                    f"**Slot:** {booking[4]}"
                )

                st.write(
                    f"**Seats:** {booking[5]}"
                )

            with col3:

                st.write(
                    f"**Total Fare:** ₹{booking[6]}"
                )

                st.write(
                    f"**Status:** {booking[7]}"
                )

            st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.info("No bookings available.")


# =========================================================
# CANCEL BOOKING
# =========================================================

elif menu == "❌ Cancel Booking":

    st.subheader("❌ Cancel Booking")

    booking_id = st.number_input(
        "Enter Booking ID",
        min_value=1,
        step=1
    )

    if st.button("Cancel Booking"):

        conn = get_connection()

        cursor = conn.cursor()

        # Check booking
        cursor.execute("""
            SELECT booking_status
            FROM bookings
            WHERE booking_id = ?
        """, (booking_id,))

        booking = cursor.fetchone()

        if booking is None:

            st.error("❌ Booking not found.")

        elif booking[0] == "Cancelled":

            st.warning("⚠️ This booking is already cancelled.")

        else:

            cursor.execute("""
                UPDATE bookings
                SET booking_status = 'Cancelled'
                WHERE booking_id = ?
            """, (booking_id,))

            conn.commit()

            st.success(
                f"✅ Booking #{booking_id} cancelled successfully."
            )

        conn.close()