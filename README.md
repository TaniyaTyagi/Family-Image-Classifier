# 🎉 Family Image Classifier

This project is a **Family Member Image Classification App** built using **Machine Learning** and **Streamlit**.  
The model predicts which family member is present in the uploaded image.

## 🧠 Project Overview

The model is trained on a dataset of family member images and classifies an uploaded image into one of the following categories:

| Label | Person Name  |
|------|--------------|
| 0    | Chote papa   |
| 1    | Lakshay      |
| 2    | Mummy        |
| 3    | Pita ji      |
| 4    | Taniya       |

The model file: `family_model.pkl`  
The app interface is built using: `Streamlit`

## 🚀 **How to Run the Project**

### 1️ Clone the Repository
```bash
git clone https://github.com/TaniyaTyagi/Family-Image-Classifier.git
cd model-6
```
2. Install Required Libraries

Make sure Python is installed, then run:

pip install streamlit numpy pillow

3. Place Model File

Ensure the family_model.pkl is located in the same directory as myfile.py.

4. Run the Streamlit App
streamlit run myfile.py

📂 File Structure
project/
│-- family_model.pkl
│-- myfile.py
│-- README.md

🖥️ User Interface Flow

Upload a family member image (.jpg, .jpeg, .png)

The model processes the image

The predicted name is displayed 🎯

📝 Code Reference

The prediction logic is implemented in myfile.py:
It loads the trained model and maps predictions to family names. 

myfile

🌟 Example Output
✅ Predicted Member Name: Mummy

💡 Future Enhancements

Improve model accuracy using a larger dataset

Add face detection for better cropping

Deploy app online using Streamlit Cloud / Heroku

🤝 Contributing

Feel free to submit improvements or suggestions.

📜 License

This project is for personal and educational use.


---

If you'd like, I can also:

✅ Create a **GitHub repository**  
✅ Generate a **PowerPoint Presentation**  
✅ Create a **Demo Video Script**  

Just tell me 👍
