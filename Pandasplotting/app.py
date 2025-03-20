from flask import Flask, Response, render_template
import pandas as pd 
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import io 

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot')
def plot():
    try:
        df=pd.read_csv('data.csv')
        plt.figure()
        df.plot()
        img=io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        return Response(img.getvalue(), mimetype='image/png')
    except FileNotFoundError:
        return "Error: data.csv not found", 404
    except Exception as e:
        return f"An error occurred: {e}", 500

if __name__== '__main__':
    app.run(debug=True)
    