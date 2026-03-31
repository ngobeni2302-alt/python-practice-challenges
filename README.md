# python-practice-challenges

This project contains a set of Python practice problems designed to improve:
- Problem-solving skills
- Understanding of loops and conditionals
- Working with lists and dictionaries
- Debugging skills

Each function must be implemented in `questions_set1.py` and validated using unit tests.

---

## 📌 QUESTIONS OVERVIEW

### 1. even_odd_tracker(numbers: list) -> list

**Goal:**  
Convert a list of integers into "Even" or "Odd".

**Input:**  
List of integers  
Example: `[1, 2, 3, 4]`

**Output:**  
List of strings  
Example: `["Odd", "Even", "Odd", "Even"]`

---

### 2. temperature_filter(temps: list) -> list

**Goal:**  
Filter temperatures between 18 and 25 (inclusive).

**Rules:**
- Ignore temperatures below -50 or above 60

**Input:**  
`[10, 18, 22, 30, 61, -100]`

**Output:**  
`[18, 22]`

---

### 3. calculate_order_total(price: int, quantity: int) -> int

**Goal:**  
Fix the buggy function.

**Rules:**
- Base fee = 10
- Total = base + (price × quantity)
- If quantity > 5 → add 20
- Minimum total = 50

**Input:**  
`price=5, quantity=2`

**Output:**  
`50`

---

### 4. process_scores(scores: list) -> str

**Goal:**  
Stop processing if a score is below 40.

**Output Cases:**
- `"Stopped early at score X"`
- `"All scores processed"`

**Example:**
- `[60, 70, 35] → "Stopped early at score 35"`
- `[45, 50, 55] → "All scores processed"`

---

### 5. organize_products(items: list) -> dict

**Goal:**  
Group products by category.

**Input:**
```python
[
  {"name": "Milk", "category": "Dairy"},
  {"name": "Cheese", "category": "Dairy"}
]

Output:

{
  "Dairy": ["Milk", "Cheese"]
}
6. sequence_growth(nums: list) -> int

Goal:
Find the length of the longest strictly increasing consecutive sequence.

Example:

[3, 4, 5, 1, 2] → 3
[5, 4, 3] → 1
▶️ HOW TO RUN TESTS
✅ Run ALL tests
python test_set1.py
✅ Run a SPECIFIC test class
python -m unittest test_set1.TestSetOne
✅ Run a SINGLE test method
python -m unittest test_set1.TestSetOne.test_even_odd_tracker
