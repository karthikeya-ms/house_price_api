# 🏡 House Price Prediction API

## 📚 Project Overview
This project implements a **Machine Learning (ML) model** for predicting **house prices** based on features such as location, income, and number of rooms. The model is **trained, optimized, and deployed as an API** using **FastAPI and Docker**.

---

## 🚀 Features
✅ **Data Preprocessing**: Cleaned and transformed housing data  
✅ **Feature Engineering**: Created useful features from raw data  
✅ **Model Training**: Trained **Random Forest & Decision Tree** regressors  
✅ **Hyperparameter Tuning**: Used **cross-validation** to optimize performance  
✅ **API Development**: Built a **FastAPI-based ML inference API**  
✅ **Dockerization**: Packaged the API into a **Docker container**  
✅ **Cloud Deployment (Planned)**: Ready for **deployment on Render/Heroku**  

---

## 📂 Project Structure
```
house_price_api/
│── data/                        # Raw & processed data
│   ├── housing.csv              # Dataset
│
│── notebooks/                    # Jupyter notebooks for EDA & modeling
│   ├── data_exploration.ipynb    # Data analysis & visualization
│
│── models/                        # Saved machine learning models
│
│── scripts/                       # API scripts
│   ├── api.py                     # FastAPI implementation
│
│── tests/                         # Placeholder for unit tests
│   ├── __init__.py                # Init file for test structure
│
│── Dockerfile                     # Docker setup for API deployment
│── requirements.txt                # Python dependencies
│── pyproject.toml                  # Poetry dependency management
│── README.md                       # Project documentation
│── LICENSE                         # License information
```

---

## ⚙️ Setup & Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/house_price_api.git
cd house_price_api
```

### **2️⃣ Install Dependencies**
```bash
poetry install
```

### **3️⃣ Run the API Locally**
```bash
poetry run uvicorn scripts.api:app --reload
```
✅ API will be available at: `http://127.0.0.1:8000`

---

## 💽 API Endpoints
### **📉 `POST /predict/`**
📚 **Predicts house prices based on input features**  
#### **Example Request**
```json
{
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 30,
    "median_income": 3.5,
    "rooms_per_household": 6,
    "bedrooms_per_room": 0.2,
    "population_per_household": 3,
    "ocean_proximity_INLAND": 0,
    "ocean_proximity_ISLAND": 0,
    "ocean_proximity_NEAR BAY": 1,
    "ocean_proximity_NEAR OCEAN": 0
}
```
#### **Example Response**
```json
{
    "predicted_house_price": 210500.0
}
```

---

## 💪 Docker Setup
### **1️⃣ Build the Docker Image**
```bash
docker build -t house_price_api .
```
### **2️⃣ Run the Docker Container**
```bash
docker run -p 8000:8000 house_price_api
```
✅ API will be available at `http://127.0.0.1:8000`

---

## 💽 Deployment (Planned)
This project is ready for **cloud deployment** on **Render / Heroku**. The following steps will be followed:

1️⃣ **Push the project to GitHub**  
2️⃣ **Connect GitHub repo to Render**  
3️⃣ **Deploy using Docker**  
4️⃣ **API will be available on a public URL**  

---

## ✅ Tasks Implemented
### **📉 Data Processing & Feature Engineering**
✔ Loaded housing data (`housing.csv`)  
✔ Handled missing values (`total_bedrooms`)  
✔ Created new features (`rooms_per_household`, `bedrooms_per_room`)  

### **👩‍💻 Model Training & Optimization**
✔ Trained **Decision Tree & Random Forest** models  
✔ Performed **Cross-Validation**  
✔ Selected **best-performing model**  

### **🏠 API Development**
✔ Built **FastAPI-based API** for predictions  
✔ Implemented **POST `/predict/` endpoint**  
✔ Tested API locally  

### **🏢 Dockerization**
✔ Created **Dockerfile**  
✔ Built & ran **Docker container**  

### **🌐 Planned Deployment**
🚧 **Deployment to Render (Pending)**  

---

## 💡 Next Steps
📌 **Deploy the API** on Render  
📌 **Implement CI/CD pipeline** for automated updates  
📌 **Optimize model performance** with feature selection  

---

---

### 📜 License
This project is licensed under the **MIT License**.

---



