from flask import Flask, request, render_template_string

app = Flask(__name__)

# ایک سادہ ایچ ٹی ایم ایل ٹیمپلیٹ جو کمزور اور محفوظ دونوں طریقوں کو دکھائے گا
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Day 8: XSS Local Lab</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #121212; color: #e0e0e0; }
        .box { background: #1e1e1e; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #333; }
        input[type="text"] { padding: 8px; width: 300px; background: #2d2d2d; color: #fff; border: 1px solid #555; }
        input[type="submit"] { padding: 8px 15px; background: #ff7b00; color: #fff; border: none; cursor: pointer; }
        .vulnerable { border-left: 4px solid #ff4444; }
        .secure { border-left: 4px solid #00C851; }
    </style>
</head>
<body>
    <h1>Day 8: Cross-Site Scripting (XSS) Lab</h1>
    <p>کوئی بھی سرچ یا ان پٹ درج کریں (مثلاً جاوا اسکرپٹ پے لوڈ):</p>
    
    <form method="GET" action="/">
        <input type="text" name="query" value="{{ query }}" placeholder="Try: <script>alert('XSS')</script>">
        <input type="submit" value="Search">
    </form>

    {% if query %}
    <div class="box vulnerable">
        <h3>1. Vulnerable Output (Using |safe filter):</h3>
        <p>You searched for: <strong>{{ query | safe }}</strong></p>
        <small style="color: #ff4444;"><i>نوٹس: یہاں پے لوڈ براہ راست ایگزیکیوٹ ہو جائے گا!</i></small>
    </div>

    <div class="box secure">
        <h3>2. Secure Output (Default Jinja2 Escaping):</h3>
        <p>You searched for: <strong>{{ query }}</strong></p>
        <small style="color: #00C851;"><i>نوٹس: یہاں فریم ورک خود بخود HTML کو اسکیپ (Escape) کر کے محفوظ رکھتا ہے۔</i></small>
    </div>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def home():
    query = request.args.get('query', '')
    return render_template_string(HTML_TEMPLATE, query=query)

if __name__ == '__main__':
    print("[*] Starting local Flask XSS Lab on http://127.0.0.1:5000")
    app.run(debug=False, port=5000)
