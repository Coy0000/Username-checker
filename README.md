# Username Validator 🧪

This simple Python script checks if a username meets certain basic rules before accepting it.

## ✅ Rules for a Valid Username:
- Must be **12 characters or fewer**
- Must **not contain any digits**
- Must **not contain any spaces**

---

## 📜 How It Works

The program asks the user to enter a username and then checks:

1. **Length Check**:
   ```python
   can't be greater than 12
   
2. **Space Check**:
   ```python
   can't contain spaces

3. **Digit Check**:
   ```python
   can't contain digits

### ✅ Valid Username
```text
  Enter your username: Alice
  welcome Alice
```

### ❌Too Long
```text
  Enter your username: verylongusername123
  username can't be greater than 12.
```
❌ Contains Digits
```text
Enter your username: John123
Username can't contain digits!
```
❌ Contains Spaces
```text
Enter your username: user name
username can't contain spaces!
```


🧑‍💻 Author
Made for learning basic Python conditionals and string methods.
