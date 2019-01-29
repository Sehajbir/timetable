from flask import Flask, render_template
app = Flask(__name__)
import datetime
import pytz
@app.route('/')
def tt():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    ist_now = utc_now.astimezone(pytz.timezone("Asia/Kolkata"))
    day = ist_now.strftime("%A")
    if day == "Monday":
        return render_template('monday.html')
    elif day == "Tuesday":
        return render_template('tuesday.html')
    elif day == "Wednesday":
        return render_template('wednesday.html')
    elif day == "Thurday":
        return render_template('thursday.html')
    elif day == "Friday":
        return render_template('friday.html')
    else:
        return render_template('day_off.html')

@app.route('/viewAll')
def tt_all():
    return render_template('tt.html')

@app.route('/service-worker.js')
def sw():
    return app.send_static_file('service-worker.js')

if __name__ == '__main__':
    app.run(debug = True)