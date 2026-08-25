from flask import Flask, jsonify

app = Flask(__name__)

# Base route ya home check ke liye
@app.route('/')
def home():
    return "Clothing Brand API is running!"

# Company Setting Endpoint (Base URL + /clothingbrand/api/v1/companySetting)
@app.route('/clothingbrand/api/v1/companySetting', methods=['GET'])
def get_company_setting():
    data = {
        "status": 200,
        "message": "Success",
        "data": {
            "shopName": "Libaas Mahal",
            "Address": "Sarafa Bazar SDK",
            "MobileNO": "03330375912",
            "Whatsapp": "03330375912",
            "email": "libaasmahal@gmail.com",
            "currency": "PKR",
            "taxPercentage": 5.0,
            "status": "Active",
            "brand_image": "https://images.unsplash.com/photo-1441986300917-64674bd600d8",
            "shop_logo": "https://images.unsplash.com/photo-1472851294608-062f824d29cc"
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
