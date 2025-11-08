# Ringkasan: Scikit-learn (Machine Learning)

Oleh : hafizhhasyhari
Tahun : 2025

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

# 1. Siapkan Data
X = df.drop('target', axis=1) # Fitur (data independen)
y = df['target']              # Target (data dependen)

# 2. Bagi Data (SANGAT PENTING!)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Preprocessing (Scaling/Encoding)
# Scaling (untuk angka)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test) # HANYA .transform() di data test!

# 4. Pilih & Latih Model
# Model Klasifikasi
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

# Model Regresi
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Model Lain
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100)

# Latih (Fit)
model.fit(X_train_scaled, y_train)

# 5. Evaluasi Model
# Prediksi
y_pred = model.predict(X_test_scaled)

# Metrik (Klasifikasi)
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Metrik (Regresi)
from sklearn.metrics import mean_squared_error
print(mean_squared_error(y_test, y_pred))

# 6. Pipeline (Cara Profesional)
# Menggabungkan preprocessing dan model
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='mean')), # Isi NaN
    ('scaler', StandardScaler()),                 # Scaling
    ('model', LogisticRegression())             # Model
])
pipeline.fit(X_train, y_train)
pipeline.score(X_test, y_test)
