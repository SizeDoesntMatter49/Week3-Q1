## 📝Question

- ร้านขายขนมปกรณ์บัวงาม ณ ห้อง 402 พ่อค้าปกรณ์อยากสร้างระบบทอนเงินอัตโนมัติ พ่อค้าปกรณ์เลยอยากให้น้องๆช่วยเขียนฟังก์ชัน ```ChangeCalculator(price,paid)``` เพื่อช่วยคำนวณว่าระบบต้องทอนเงินเป็นธนบัตรและเหรียญเป็นจำนวณเท่าใด คืนให้ลูกค้า โดยใช้แบงค์/เหรียญให้น้อยที่สุด
- แบงค์และเหรียญมีดังนี้ ```[1000,500,100,50,20,10,5,1]```

## 📥Input

Input ของฟังก์ชันจะมี 2 ตัวแปร เป็นตัวแปรได้แก่ 
- ```price``` คือราคาขนมที่ต้องจ่าย 
- ```paid``` คือจำนวนเงินที่ลูกค้าจ่ายมา 
- **ทั้ง 2 ตัวแปรต้องเป็นจำนวนเต็มบวกเท่านั้น**


## 📤Output
- หาก user input ข้อมูลไม่ถูกต้องให้ return ```"ERROR"```
- หาก ```paid``` น้อยกว่า ```price``` ให้ return ```"ERROR"```
- return ค่าคำตอบในรูปแบบของ array ที่มีสมาชิกเป็นจำนวนแบงค์หรือเหรียญนั้นๆ โดยเรียงลำดับตาม list ของแบงค์และเหรียญที่ได้ชี้แจงไว้ข้างต้น

    - ตัวอย่าง : 
        - INPUT : ```ChangeCalculator(4567,5000)```
        - วิธีคิด : 5000 - 4567 = 433 : จ่าย ```100฿x4 20฿x1 10฿x1 1฿x3```
        - OUTPUT : ```[0,0,4,0,1,1,0,3]```


## ⚙️Function
The function is defined in the file ```ChangeCalculator.py``` as the following:
>จงเขียนฟังก์ชันนี้ด้วยภาษา Python

```python
def ChangeCalculator(price,paid):

    return [0]*8
```

## 💡 Example 01
**Input**  
```python
ChangeCalculator(100,500)
```

**Output**
```python
[0,0,4,0,0,0,0,0]
```

## 💡 Example 02
**Input**  
```python
ChangeCalculator(123, 1711)
```

**Output**
```python
[1,1,0,1,1,1,1,3]
```


## ▶️ To Run a Test Case  

### 🪟 Windows 
    run a file name "Run_Window.ps1"
### 🍎 macOS
    run a file name "Run_macOS.sh"

## 🚨 Importance  

⚠️ **Always commit and push your code to origin before calling the TA to submit your quiz!**  
🚀 This ensures your latest work is saved and reviewed correctly.
