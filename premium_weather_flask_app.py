from flask import Flask
import requests

app = Flask(__name__)

API_KEY = "cd45146fa2ff4c32a39194004261604"
CITY = "Kopargaon"


@app.route("/")
def home():

    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={CITY}&days=7"
    data = requests.get(url).json()

    current = data["current"]
    forecast = data["forecast"]["forecastday"]

    temp = round(current["temp_c"])
    feels = round(current["feelslike_c"])
    humidity = current["humidity"]
    wind = round(current["wind_kph"])
    pressure = round(current["pressure_mb"])
    desc = current["condition"]["text"]

    sunrise = forecast[0]["astro"]["sunrise"]
    sunset = forecast[0]["astro"]["sunset"]

    rows = ""
    days = ["Today", "Sat", "Sun", "Mon", "Tue", "Wed", "Thu"]

    for i, day in enumerate(forecast):
        maxt = round(day["day"]["maxtemp_c"])
        mint = round(day["day"]["mintemp_c"])

        rows += f"""
        <div class='row'>
            <div>{days[i]}</div>
            <div>☀️</div>
            <div>{mint}°</div>
            <div class='bar'><span></span></div>
            <div>{maxt}°</div>
        </div>
        """

    html = f"""
<html>
<head>
<title>Weather Ultra Sky</title>

<style>

* {{
margin:0;
padding:0;
box-sizing:border-box;
font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
}}

body {{
background:
radial-gradient(circle at 20% 15%, rgba(255,255,255,.08), transparent 18%),
radial-gradient(circle at 75% 12%, rgba(255,255,255,.06), transparent 16%),
radial-gradient(circle at 50% 35%, rgba(80,120,255,.08), transparent 25%),
linear-gradient(to bottom,
#02030d 0%,
#06153a 18%,
#0b2360 42%,
#123b8a 72%,
#275dc2 100%);
min-height:100vh;
color:white;
overflow-x:hidden;
position:relative;
}}

body:before {{
content:'';
position:fixed;
inset:0;
pointer-events:none;
background:
radial-gradient(circle at 5% 10%, rgba(255,255,255,.95) 0 1px, transparent 2px),
radial-gradient(circle at 15% 30%, rgba(255,255,255,.85) 0 1.2px, transparent 2px),
radial-gradient(circle at 25% 20%, rgba(255,255,255,.95) 0 1px, transparent 2px),
radial-gradient(circle at 40% 12%, rgba(255,255,255,.75) 0 1px, transparent 2px),
radial-gradient(circle at 55% 18%, rgba(255,255,255,.95) 0 1.4px, transparent 3px),
radial-gradient(circle at 70% 10%, rgba(255,255,255,.8) 0 1px, transparent 2px),
radial-gradient(circle at 82% 25%, rgba(255,255,255,.9) 0 1.2px, transparent 2px),
radial-gradient(circle at 92% 14%, rgba(255,255,255,.7) 0 1px, transparent 2px),
radial-gradient(circle at 10% 60%, rgba(255,255,255,.8) 0 1px, transparent 2px),
radial-gradient(circle at 30% 70%, rgba(255,255,255,.9) 0 1.2px, transparent 2px),
radial-gradient(circle at 60% 65%, rgba(255,255,255,.8) 0 1px, transparent 2px),
radial-gradient(circle at 85% 75%, rgba(255,255,255,.95) 0 1.2px, transparent 2px);
animation:twinkle 5s ease-in-out infinite alternate;
opacity:1;
}}

@keyframes twinkle {{
0% {{opacity:.55; transform:translateY(0px);}}
100% {{opacity:1; transform:translateY(-2px);}}
}}

.wrap {{
max-width:460px;
margin:auto;
padding:30px 15px 60px;
}}

.hero {{
text-align:center;
padding-top:12px;
}}

.loc {{
font-size:14px;
opacity:.85;
}}

.city {{
font-size:56px;
font-weight:700;
margin-top:6px;
}}

.temp {{
font-size:165px;
font-weight:200;
line-height:1;
text-shadow:0 0 18px rgba(255,255,255,.15);
}}

.desc {{
font-size:30px;
margin-top:-10px;
}}

.range {{
font-size:18px;
opacity:.9;
margin-top:4px;
}}

.card {{
margin-top:18px;
background:rgba(255,255,255,.11);
backdrop-filter:blur(24px);
border-radius:28px;
padding:20px;
border:1px solid rgba(255,255,255,.12);
box-shadow:0 10px 35px rgba(0,0,0,.18);
}}

.note {{
font-size:17px;
line-height:1.45;
margin-bottom:18px;
}}

.hourly {{
display:flex;
gap:12px;
overflow-x:auto;
padding-bottom:5px;
}}

.hourly::-webkit-scrollbar {{
display:none;
}}

.hour {{
min-width:72px;
text-align:center;
}}

.time {{
font-size:14px;
opacity:.8;
margin-bottom:8px;
}}

.icon {{
font-size:26px;
margin-bottom:8px;
}}

.degree {{
font-size:18px;
}}

.title {{
font-size:13px;
opacity:.75;
margin-bottom:12px;
font-weight:700;
}}

.row {{
display:grid;
grid-template-columns:70px 30px 45px 1fr 45px;
gap:10px;
align-items:center;
padding:13px 0;
border-bottom:1px solid rgba(255,255,255,.08);
}}

.row:last-child {{
border:none;
}}

.bar {{
height:8px;
background:rgba(255,255,255,.14);
border-radius:50px;
overflow:hidden;
}}

.bar span {{
display:block;
height:100%;
width:80%;
border-radius:50px;
background:linear-gradient(to right,#ffe66d,#ffb703,#ff7b00,#ff3d00);
}}

.grid {{
display:grid;
grid-template-columns:1fr 1fr;
gap:14px;
margin-top:18px;
}}

.box {{
background:rgba(255,255,255,.11);
border-radius:24px;
padding:18px;
min-height:120px;
border:1px solid rgba(255,255,255,.08);
}}

.label {{
font-size:13px;
opacity:.75;
}}

.value {{
font-size:38px;
font-weight:700;
margin-top:10px;
}}

.sub {{
font-size:13px;
opacity:.75;
}}

</style>
</head>

<body>

<div class="wrap">

<div class="hero">
<div class="loc">📍 HOME</div>
<div class="city">{CITY}</div>
<div class="temp">{temp}°</div>
<div class="desc">{desc}</div>
<div class="range">H:{temp+4}°   L:{temp-5}°</div>
</div>

<div class="card">
<div class="note">
Partly cloudy conditions expected tonight.<br>
Feels like {feels}°. Wind gusts up to {wind} kph.
</div>

<div class="hourly">
<div class="hour"><div class="time">Now</div><div class="icon">🌙</div><div class="degree">{temp}°</div></div>
<div class="hour"><div class="time">1AM</div><div class="icon">☁️</div><div class="degree">{temp-1}°</div></div>
<div class="hour"><div class="time">2AM</div><div class="icon">☁️</div><div class="degree">{temp-2}°</div></div>
<div class="hour"><div class="time">3AM</div><div class="icon">🌙</div><div class="degree">{temp-3}°</div></div>
<div class="hour"><div class="time">4AM</div><div class="icon">☁️</div><div class="degree">{temp-4}°</div></div>
</div>
</div>

<div class="card">
<div class="title">10-DAY FORECAST</div>
{rows}
</div>

<div class="grid">

<div class="box">
<div class="label">Sunrise</div>
<div class="value" style="font-size:28px;">{sunrise}</div>
<div class="sub">Morning</div>
</div>

<div class="box">
<div class="label">Sunset</div>
<div class="value" style="font-size:28px;">{sunset}</div>
<div class="sub">Evening</div>
</div>

<div class="box">
<div class="label">Humidity</div>
<div class="value">{humidity}%</div>
<div class="sub">Current</div>
</div>

<div class="box">
<div class="label">Pressure</div>
<div class="value">{pressure}</div>
<div class="sub">hPa</div>
</div>

</div>

</div>

</body>
</html>
"""
    return html


if __name__ == "__main__":
    app.run(debug=True)