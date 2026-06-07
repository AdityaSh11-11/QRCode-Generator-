import streamlit as st
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image
from io import BytesIO


st.set_page_config(page_title="QR Code Generator", page_icon="🔳", layout="centered")
st.markdown(
    """
    <style>
    /* Entire app background */
    .stApp {
        background-color: #0b1f3a;  /* Dark Blue */
        color: white;
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: #081a2f;
    }

    /* Text color override */
    html, body, [class*="css"] {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='text-align: center;
               color: white;
               font-size: 42px;
               font-weight: bold;
               margin-bottom: 10px;'>
        QR Code Generator App
    </h1>
    """,
    unsafe_allow_html=True
)


data = st.text_area("Provide Some Links or URLs")


col1, col2 = st.columns(2)

with col1:
    fill_color = st.color_picker("QR Color", "#000000")

with col2:
    back_color = st.color_picker("Background Color", "#ffffff")


if st.button("Generate QR Code"):

    if data.strip() == "":
        st.error("Please enter some text or URL")
    else:
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        buf = BytesIO()
        img.save(buf, "PNG")
        byte_im = buf.getvalue()

        st.image(byte_im, caption="Generated QR Code", use_container_width=True)

        st.download_button(
            label="⬇ Download QR Code",
            data=byte_im,
            file_name="qr_code.png",
            mime="image/png"
        )


st.markdown(
    """
    <style>
    .custom-footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #2f2f2f;
        color: #ffffff;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        z-index: 9999;
    }
    </style>

    <div class="custom-footer">
        © 2026 | QR Code Generator App | Developed by Aditya Sharma    </div>
    """,
    unsafe_allow_html=True
)