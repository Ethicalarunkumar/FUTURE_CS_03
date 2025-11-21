from flask import Flask, render_template_string, request, send_file
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML = """
<h2>🔐 Secure File Sharing System</h2>

<form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <button type="submit">Upload & Encrypt</button>
</form>

<h3>📥 Download Files</h3>
<ul>
    {% for f in files %}
        <li><a href="/download/{{ f }}">{{ f }}</a></li>
    {% endfor %}
</ul>
"""

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        encrypted_path = filepath + ".enc"
        encrypt_file(filepath, encrypted_path)
        os.remove(filepath)

    files = os.listdir(UPLOAD_FOLDER)
    return render_template_string(HTML, files=files)

@app.route("/download/<filename>")
def download(filename):
    enc_path = os.path.join(UPLOAD_FOLDER, filename)
    dec_path = "decrypted_" + filename.replace(".enc", "")

    decrypt_file(enc_path, dec_path)
    return send_file(dec_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
