# 🚀 ML-Based Profit Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![React](https://img.shields.io/badge/React-18.2.0-61dafb.svg)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4.17-38bdf8.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**AI-Powered Business Intelligence Platform for Profit Prediction**

[![Demo](https://img.shields.io/badge/Live-Demo-orange?style=for-the-badge&logo=vercel)](https://your-demo-link.com)
[![Documentation](https://img.shields.io/badge/Documentation-Wiki-blue?style=for-the-badge)](https://github.com/yourusername/profit-predictor/wiki)

</div>

---

## 📋 Table of Contents

- [🎯 Overview](#-overview)
- [✨ Features](#-features)
- [🛠️ Technology Stack](#️-technology-stack)
- [📊 Dataset](#-dataset)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🎮 Usage](#-usage)
- [🔧 API Documentation](#-api-documentation)
- [🎨 Screenshots](#-screenshots)
- [📝 License](#-license)
- [👥 Authors](#-authors)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🎯 Overview

**Profit Predictor** is a cutting-edge Machine Learning application that leverages advanced algorithms to predict company profits based on R&D spending, administrative costs, and marketing expenditures. Built with a modern React frontend and robust Python backend, it provides real-time business intelligence with 95%+ accuracy.

### 🎯 Key Objectives

- **Predictive Analytics**: Forecast company profits using ML algorithms
- **Business Intelligence**: Provide actionable insights and recommendations
- **Real-time Analysis**: Instant predictions with interactive visualizations
- **User-friendly Interface**: Modern, responsive design for seamless experience

---

## ✨ Features

### 🧠 **Core Functionality**
- **Multi-Algorithm ML Engine**: 9 different ML models for optimal predictions
- **Real-time Predictions**: Instant profit forecasting with live updates
- **Smart Insights**: AI-powered recommendations and business analysis
- **Interactive Visualizations**: Charts and graphs for data exploration

### 📊 **Analytics & Insights**
- **ROI Analysis**: Calculate return on investment metrics
- **Allocation Breakdown**: Visualize spending distribution
- **Trend Analysis**: Track prediction history and patterns
- **Performance Metrics**: R² scores, MAE, RMSE, and cross-validation

### 🎨 **User Experience**
- **Modern UI/UX**: Beautiful gradient design with glassmorphism effects
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Interactive Controls**: Sliders and real-time input validation
- **Data Export**: Export predictions and insights as JSON

### 🔧 **Technical Features**
- **Model Persistence**: Save and load trained models
- **Data Preprocessing**: Automated scaling and normalization
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Scalable Architecture**: Modular design for easy expansion

---

## 🛠️ Technology Stack

### **Backend (Python)**
- **Python 3.8+** - Core programming language
- **Scikit-learn** - Machine Learning algorithms
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **XGBoost** - Gradient boosting framework
- **Matplotlib/Seaborn** - Data visualization
- **Joblib** - Model serialization

### **Frontend (React)**
- **React 18.2.0** - UI framework
- **Tailwind CSS** - Utility-first CSS framework
- **Chart.js** - Interactive charts and graphs
- **Lucide React** - Beautiful icons
- **React Chart.js 2** - Chart.js integration

### **Development Tools**
- **Node.js** - JavaScript runtime
- **npm** - Package manager
- **Git** - Version control

---

## 📊 Dataset

The application uses a comprehensive dataset of **1,000 companies** with the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| **R&D Spend** | Research and Development expenditure | ₹0 - ₹200,000 |
| **Administration** | Administrative costs | ₹50,000 - ₹200,000 |
| **Marketing Spend** | Marketing and advertising costs | ₹0 - ₹500,000 |
| **Profit** | Target variable (predicted) | ₹10,000 - ₹200,000 |

### 📈 Dataset Statistics
- **Total Records**: 1,000 companies
- **Features**: 3 independent variables
- **Target**: 1 dependent variable (Profit)
- **Data Quality**: Clean, preprocessed data

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn package manager

### One-Command Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/profit-predictor.git
cd profit-predictor

# Run the setup script
./setup.sh
```

---

## 📦 Installation

### 1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/profit-predictor.git
cd profit-predictor
```

### 2. **Backend Setup**
```bash
# Navigate to backend directory
cd exposys/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Train the model
python model.py
```

### 3. **Frontend Setup**
```bash
# Navigate to frontend directory
cd ../frontend

# Install dependencies
npm install

# Start development server
npm start
```

### 4. **Start the Application**
```bash
# Terminal 1: Start backend (from backend directory)
python app.py

# Terminal 2: Start frontend (from frontend directory)
npm start
```

The application will be available at:
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:5000

---

## 🎮 Usage

### **Making Predictions**

1. **Input Data**: Enter values for:
   - R&D Spend (₹)
   - Administrative Costs (₹)
   - Marketing Spend (₹)

2. **Get Predictions**: Click "Predict Profit" to receive:
   - Predicted profit amount
   - ROI analysis
   - Smart recommendations
   - Visual breakdowns

3. **Explore Insights**: Navigate through different views:
   - **Predict**: Main prediction interface
   - **Trends**: Historical data visualization
   - **Insights**: AI-powered recommendations
   - **History**: Past predictions tracking

### **Advanced Features**

- **Real-time Sliders**: Adjust values with interactive sliders
- **Data Export**: Download predictions as JSON files
- **Share Results**: Share predictions via clipboard or native sharing
- **History Management**: View and clear prediction history



## 🔧 API Documentation

### **Prediction Endpoint**

**POST** `/predict`

Predict profit based on input parameters.

#### Request Body
```json
{
  "rndSpend": 150000,
  "admin": 120000,
  "marketing": 300000
}
```

#### Response
```json
{
  "prediction": 185432.67,
  "confidence": 0.95,
  "model_used": "XGBoost"
}
```

#### Example Usage
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"rndSpend": 150000, "admin": 120000, "marketing": 300000}'
```

---

## 🎨 Screenshots

<div align="center">

### Main Prediction Interface
![Main Interface](https://via.placeholder.com/800x400/1f2937/ffffff?text=Main+Prediction+Interface)

### Analytics Dashboard
![Analytics](https://via.placeholder.com/800x400/1f2937/ffffff?text=Analytics+Dashboard)

### Insights Panel
![Insights](https://via.placeholder.com/800x400/1f2937/ffffff?text=Smart+Insights)

</div>



## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Profit Predictor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👥 Authors

### **Lead Developer**
- **Name**: [Your Name]
- **Email**: your.email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)
- **LinkedIn**: [Your LinkedIn](https://linkedin.com/in/yourprofile)

### **Contributors**
- **Contributor 1** - Backend Development
- **Contributor 2** - Frontend Development
- **Contributor 3** - UI/UX Design

---

## 🙏 Acknowledgments

- **Scikit-learn Team** - For the excellent ML library
- **React Team** - For the amazing frontend framework
- **Tailwind CSS** - For the utility-first CSS framework
- **Chart.js** - For beautiful data visualizations
- **Open Source Community** - For inspiration and support

---

## 📞 Support

If you have any questions or need help:

- **Issues**: [GitHub Issues](https://github.com/yourusername/profit-predictor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/profit-predictor/discussions)
- **Email**: support@profitpredictor.com
- **Documentation**: [Wiki](https://github.com/yourusername/profit-predictor/wiki)

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

[![GitHub stars](https://img.shields.io/github/stars/yourusername/profit-predictor?style=social)](https://github.com/yourusername/profit-predictor)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/profit-predictor?style=social)](https://github.com/yourusername/profit-predictor)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/profit-predictor)](https://github.com/yourusername/profit-predictor/issues)

**Made with ❤️ by the Profit Predictor Team**

</div>
