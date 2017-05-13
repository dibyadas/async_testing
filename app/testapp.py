import time
from flask import Flask, redirect, url_for, request, render_template, Response
from multiprocessing import Pool


app = Flask(__name__)

def test():
	print("start")
	time.sleep(7)
	print("end")


@app.route("/")
def dpd():
	pool = Pool(processes=1)
	r = pool.apply_async(test)
	return ("done",200,{'Access-Control-Allow-Origin':'*'})





if __name__ == "__main__":  # This is for local testin
    app.run(host='localhost', port=3453, debug=True)
