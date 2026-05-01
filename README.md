# 🌐 FastAPI Deployment

This project has also been deployed using FastAPI and Render to provide live regression predictions through REST API endpoints.

The deployed API allows users to:

* Test the regression model online
* Send input values dynamically
* Receive prediction outputs instantly
* Interact with the model using FastAPI Swagger documentation

---

# 🚀 Live Deployment

## 🔗 Live API

```
https://basic-regression-project-from-scratch.onrender.com
```

## 📄 Interactive API Documentation

```
https://basic-regression-project-from-scratch.onrender.com/docs
```

The `/docs` endpoint provides an interactive Swagger UI generated automatically by FastAPI where users can test the regression prediction endpoints directly from the browser.

---

# ⚡ FastAPI Integration

The regression model was integrated with FastAPI to expose machine learning predictions through API endpoints.

Example endpoint:

```python id="f3m7jk"
@app.get("/predict")
def predict(value: float):
```

Users can provide input values and receive regression predictions in JSON format.

---

# 📌 Example API Response

```json id="r2x6mn"
{
  "input": 5,
  "prediction": 487.40469783807
}
```

---

# 🧠 Why FastAPI Was Used

FastAPI was used to:

* Convert the ML model into a deployable web API
* Enable real-time prediction access
* Create automatic interactive API documentation
* Simulate production-level ML deployment workflows

This transforms the project from a local notebook-based model into a live machine learning application accessible online.

---

# ☁️ Deployment Stack

This project was deployed using:

* FastAPI
* Uvicorn
* Render
* Scikit-learn

---

# 🔄 Deployment Workflow

```text id="4d8yjk"
User Input
   ↓
FastAPI Endpoint
   ↓
Regression Model
   ↓
Prediction Response
```

---

# 🎯 Deployment Learning Outcomes

Through this deployment process, the project demonstrates:

* Machine Learning model deployment
* REST API development
* Backend integration using FastAPI
* Cloud deployment using Render
* Real-time prediction serving

---

# 💡 Future Improvements

* Add POST request support
* Deploy multiple ML models
* Add frontend UI using Streamlit
* Dockerize the application
* Add model monitoring and logging
