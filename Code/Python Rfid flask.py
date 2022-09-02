import serial
from flask import Flask
        
app = Flask(__name__)

@app.route('/')
def main():
    with serial.Serial("/dev/cu.usbmodem141201", 9600) as ser:
        line = ser.readline().decode("utf-8")
        print(line)
        
        try:
            a = line.split(";")
            a = map(lambda x: x.split(","), a)

            return str(line)+"<script>location.reload()</script>"
        finally:
            pass
        
if __name__ == '__main__':
    app.run(debug=True)