# Flutter App

This is the Flutter mobile app in the `flutter-iot-template` project.

---

## 🧪 Hello World + FastAPI API Call

This app demonstrates:

- A simple "Hello from Flutter!" message by default
- Fetching a greeting from a FastAPI backend endpoint `/hello` on startup

---

## ⚙️ Install & Run

### 🔹 Prerequisites

- [Flutter SDK](https://docs.flutter.dev/get-started/install) (version 3.0+ recommended)
- Android Studio / iOS Simulator / Physical device

---

### 🔹 Option 1: Install Flutter SDK

#### 🐧 On Linux

```bash
curl -O https://storage.googleapis.com/flutter_infra_release/releases/stable/linux/flutter_linux_3.22.1-stable.tar.xz
tar xf flutter_linux_3.22.1-stable.tar.xz
export PATH="$PATH:`pwd`/flutter/bin"
flutter --version
```

#### 🪟 On Windows (PowerShell)

1. Download from https://docs.flutter.dev/get-started/install/windows
2. Extract and add `flutter/bin` to your PATH
3. Run: `flutter --version`

---

### 🔹 Option 2: Run the App

```bash
cd flutter_app
flutter pub get
flutter run
```

✅ Make sure a device or emulator is running!

---

## 🔄 API Integration

The app sends an HTTP GET request to the FastAPI backend:

```
GET http://10.0.2.2:8000/hello
```

📌 Note: On Android emulators, use `10.0.2.2` instead of `localhost`.

---

## 📦 Dependencies

```yaml
dependencies:
  http: ^0.13.6
```

---

## 🔍 API Integration Code Explanation

The following logic is implemented in `lib/main.dart`:

### 🔹 1. Importing HTTP and JSON packages

```dart
import 'package:http/http.dart' as http;
import 'dart:convert';
```

- `http`: For making HTTP requests
- `json.decode`: To parse the JSON response from FastAPI

---

### 🔹 2. API Request Function

```dart
Future<void> _fetchHelloMessage() async {
  final response = await http.get(Uri.parse('http://10.0.2.2:8000/hello'));
  ...
}
```

- `http.get(...)`: Sends a GET request to the FastAPI server
- `10.0.2.2`: Refers to your local machine when using an Android emulator
- On a successful response, it parses the response and stores the message in state

---

### 🔹 3. Updating the UI State

```dart
setState(() {
  _message = data['message'] ?? 'No message';
});
```

- Updates the `_message` variable with the fetched text
- Automatically triggers a UI refresh in Flutter

---

### 🔹 4. Displaying the Result

```dart
body: Center(child: Text(_message));
```

- Displays the fetched message in the center of the screen
- Shows `'Loading...'` initially and then updates with the API result
