from flask import Flask, Response, render_template
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import io

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/histogram')
def histogram():
    try:
        df=pd.read_csv('data.csv')
        plt.figure()
        df['Duration'].plot(kind='hist')
        img=io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()
        return Response(img.getvalue(),mimetype='image/png')
    except FileNotFoundError:
        return "Error: data.csv not found", 404
    except KeyError:
        return "Error:'Duration' column not found in data.csv", 400
    except Exception as e:
        return f"An error occurred:{e}", 500

if __name__== '__main__':
    app.run(debug=True)