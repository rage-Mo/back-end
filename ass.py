from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def render_index_page():
    # Write your code here
    return render_template('dv1.html')


@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name')
    ip_address = request.remote_addr
    location = requests.get('https://freegeoip.app/json/').json()
    city = location["city"]
    temperature = 11  # Replace with actual temperature data
    message = f'Client_ip : ({ip_address}) Location : {city} greeting : Hello, {visitor_name}! The temperature is {temperature} degrees in {city}.'
    return jsonify({'message': message})
    
    
   
      
   
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

