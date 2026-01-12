from flask import Flask
# Kita import file calc.py yang ada di folder sources
from sources import calc 

app = Flask(__name__)

@app.route('/')
def home():
    # Kita pake fungsi add2 dari calc.py (5 + 5)
    hasil = calc.add2(5, 5)

    # Ini HTML yang bakal muncul di browser
    return f"""
    <html>
        <head>
            <title>Submission CI/CD Eed</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; padding-top: 50px; }}
                .card {{ border: 1px solid #ddd; padding: 20px; display: inline-block; border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
                h1 {{ color: #2E86DE; }}
                .badge {{ background-color: #27ae60; color: white; padding: 5px 10px; border-radius: 5px; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Dicoding CI/CD Pipeline</h1>
                <p>Deployed by <strong>Moh. Suaidi</strong> via Jenkins & Vercel</p>
                <hr>
                <h3>Test Integrasi Fungsi Python:</h3>
                <p>Hasil perhitungan <code>5 + 5</code> dari modul <em>calc.py</em> adalah:</p>
                <h2 class="badge">{hasil}</h2>
            </div>
        </body>
    </html>
    """

# Baris ini penting biar Vercel tau cara jalanin app-nya
if __name__ == '__main__':
    app.run()
